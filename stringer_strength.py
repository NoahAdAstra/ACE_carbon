from openpyxl import load_workbook
import numpy as np
import os
import starting_values as val

#########################################################################################
A_matrix_stringer = [[172517.98,54088.62,0.00],
                     [54088.62,172517.98,0.00],
                     [0.00,0.00,59214.68]]

B_matrix_stringer = [[0,0,0],[0,0,0],[0,0,0]]

D_matrix_stringer = [[113389.70,62839.36,18839.82],
                     [62839.36, 88269.94, 18839.82],
                     [18839.82, 18839.82, 66541.71]]


A_matrix_invers = np.linalg.inv(A_matrix_stringer) 
#B_matrix_invers = np.linalg.inv(B_matrix_stringer) 
D_matrix_invers = np.linalg.inv(D_matrix_stringer) 
###########################################################################################


E_homo_top = A_matrix_stringer[0][0]/val.stringer_thikness
G_homo_top = A_matrix_stringer[2][2]/val.stringer_thikness

E_homo_bottom = 1/(A_matrix_invers[0][0]*val.stringer_thikness)
E_homo_bottom = 1/(A_matrix_invers[2][2]*val.stringer_thikness)

term_1 = (E_homo_top * val.stringer_dim_1*val.stringer_thikness) +  (E_homo_bottom * val.stringer_dim_2*val.stringer_thikness)
term_2 = (val.stringer_dim_1*val.stringer_thikness) + (val.stringer_dim_2*val.stringer_thikness)
E_homo_ges = term_1/term_2


#___setting up the data base__
if __name__ == '__main__': 
    os.chdir('../../03_FemResults')

femdir = os.getcwd()
print(os.getcwd())


maindir_stringer_strength= {} 
for i in range (1,4):
    maindir_stringer_strength.update({f'LC{i}':{}})
    for j in range (1,9):
        maindir_stringer_strength [f'LC{i}'].update({f'Ply{j}':{}}) 

deg_list = [45,-45,0,90,90,0,-45,45]

#___get values___
file_path = os.path.join(femdir, f'{val.filename_strength_stringer}.xlsx')
wb = load_workbook(file_path)
ws = wb[val.filename_strength_stringer]

column = 5
row = 0

for LoadCases in maindir_stringer_strength:
    row += 12
    i = 0
    for Ply,SpecificPly in maindir_stringer_strength[LoadCases].items():
        epsilon_stringer = ws.cell(row=row,column=column).value
        SpecificPly.update({'epsilon_stringer':epsilon_stringer})
        SpecificPly.update({'phi_d':deg_list[i]})
        i += 1


#___calculate sigma ply__
for LoadCases in maindir_stringer_strength:
    for Ply,SpecificPly in maindir_stringer_strength[LoadCases].items():
        phi = SpecificPly['phi_d']
        epsilon_ply = (np.cos(phi)**2) * SpecificPly['epsilon_stringer']
        sigma_ply = E_homo_ges * epsilon_ply  
        SpecificPly.update({'sigma_ply':sigma_ply})

for LoadCases in maindir_stringer_strength:
    for Ply,SpecificPly in maindir_stringer_strength[LoadCases].items():
        sigma_x = SpecificPly['sigma_ply']
        if  sigma_x >= 0:
            RF_FF = 1/(sigma_x/val.R_paralel_t)
        else:
            RF_FF = 1/(sigma_x/-val.R_paralel_c)
        
        SpecificPly.update({'mode':'FF'})
        SpecificPly.update({'RF_FF': RF_FF})
        SpecificPly.update({'RF_IFF':'infinite'})
        SpecificPly.update({'RF_comb': RF_FF})

print('helo')