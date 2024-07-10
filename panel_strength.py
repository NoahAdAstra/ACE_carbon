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
###########################################################################################




#___setting up the data base__
os.chdir('../../03_FemResults')
femdir = os.getcwd()
print(os.getcwd())

cases = ['LC1','LC2','LC3',]
LC1dir ={}
LC2dir ={}
LC3dir ={}

maindir_panel_strength = {}
maindir_panel_strength ['LC1'] = LC1dir
maindir_panel_strength ['LC2'] = LC2dir
maindir_panel_strength ['LC3'] = LC3dir

for i in range (1,4):
    for j in range (1,9):
        maindir_panel_strength [f'LC{i}'] = {}


#__get values for panel strength___
#___ply X___
file_path = os.path.join(femdir, f'{val.filename_strength_panels_x}.xlsx')
wb = load_workbook(file_path)
ws = wb[val.filename_strength_panels_x]


column = 6
row = -228
for LoadCases in maindir_panel_strength:
    row += 240
    for j in range(0,8): 
        id = {}
        id ['sigma_x'] = ws.cell(row=row+j*30,column=column).value
        maindir_panel_strength [LoadCases] [f'Ply{j+1}'] = id


#___ply Y___         
file_path = os.path.join(femdir, f'{val.filename_strength_panels_y}.xlsx')
wb = load_workbook(file_path)
ws = wb[val.filename_strength_panels_y]

column = 6
row = -228
for LoadCases in maindir_panel_strength:
    row += 240
    for j in range(0,8): 
        hey = ws.cell(row=row+j*30,column=column).value
        maindir_panel_strength [LoadCases] [f'Ply{j+1}'].update({'sigma_y': hey})

#___ply XY___         
file_path = os.path.join(femdir, f'{val.filename_strength_panels_xy}.xlsx')
wb = load_workbook(file_path)
ws = wb[val.filename_strength_panels_xy]

column = 6
row = -228
for LoadCases in maindir_panel_strength:
    row += 240
    for j in range(0,8): 
        hey = ws.cell(row=row+j*30,column=column).value
        maindir_panel_strength [LoadCases] [f'Ply{j+1}'].update({'tau': hey})

#___FF RF___

for LoadCases in maindir_panel_strength:
    for Ply in maindir_panel_strength[LoadCases]: 
        sigma_x = maindir_panel_strength[LoadCases][Ply]['sigma_x']
        if  sigma_x >= 0:
            RF_FF = 1/(sigma_x/val.R_paralel_t)
        else:
            RF_FF = 1/(sigma_x/-val.R_paralel_c)
        maindir_panel_strength[LoadCases][Ply].update({'RF_FF':RF_FF})
        
#___IFF RF___
R_paralel_A = val.R_perpendicular_c/(2*(1+val.p_weird))
tau_C = val.R_shear*((1+(2*val.p_weird))**0.5)

for LoadCases in maindir_panel_strength:
    for Ply in maindir_panel_strength[LoadCases]:  
        sigma_y = maindir_panel_strength[LoadCases][Ply]['sigma_y']
        tau = maindir_panel_strength[LoadCases][Ply]['tau']
        if sigma_y >= 0:
            maindir_panel_strength[LoadCases][Ply].update({'mode':'A'})
            (((tau/val.R_shear)**2)+((1-val.p_weird*())**2))
        if sigma_y < 0 and abs(sigma_y/tau) <= (R_paralel_A/abs(tau_C)):
            maindir_panel_strength[LoadCases][Ply].update({'mode':'B'})

        if sigma_y < 0 and abs(tau/sigma_y) <= (abs(tau_C)/R_paralel_A):
            maindir_panel_strength[LoadCases][Ply].update({'mode':'C'})
 print()



