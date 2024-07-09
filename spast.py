from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import Alignment
from openpyxl.utils import column_index_from_string,get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
import numpy as np

import logging
import os

### 
'''  knockdown values !!!!!!!!!!!!  '''
###

######################################################################################################################
E_11 = 135369.47
E_22 = 10413.04
G_12 = 5206.52

v_12 = 0.33
v_21 = (v_12 * E_22)/E_11

a_width = 600 #m
b_length = 400 #m
t_thikness = 1.104*8

m_mave = 2
n_wave = 1

filename_stability_panels = 'stability_panels'
######################################################################################################################


#___calculating the A,B,D matrixes___

Q_11 = E_11/(1-(v_12*v_21))
Q_22 = E_22/(1-(v_12*v_21))
Q_12 = (v_21*E_11)/(1-(v_12*v_21))
Q_66 = G_12

Q = [[Q_11,Q_12,0],
     [Q_12,Q_22,0],
     [0 , 0 ,Q_66]]

'''def T(phi_d):
    phi = np.deg2rad(phi_d)
    T = [[np.cos(phi)**2 , np.sin(phi)**2 , 2*np.sin(phi)*np.cos(phi)],
        [np.sin(phi)**2 , np.cos(phi)**2 , -2*np.sin(phi)*np.cos(phi)],
        [-1*np.sin(phi)*np.cos(phi) , np.sin(phi)*np.cos(phi), ((np.cos(phi)**2)-(np.sin(phi)**2))]]
    T_trans = np.transpose(T)
    return T_trans

def T_1(phi_d):
    phi = np.deg2rad(phi_d)
    T = [[np.cos(phi)**2 , np.sin(phi)**2 , -2*np.sin(phi)*np.cos(phi)],
        [np.sin(phi)**2 , np.cos(phi)**2 , 2*np.sin(phi)*np.cos(phi)],
        [np.sin(phi)*np.cos(phi) , -1*np.sin(phi)*np.cos(phi), ((np.cos(phi)**2)-(np.sin(phi)**2))]]
    return T

def Q_strich(phi):
    zwichen = np.dot(T_1(phi),Q)
    result = np.dot(zwichen,T(phi))
    return result

Q_ply_1 = Q_strich(45)
'''
#ply height 1.104
Z_hoehe = [-4.416,-3.312,-2.208,-1.104,0,1.104,2.208,3.312,4.416]

A_matrix = [[637213.62,243398.79,69558.64],
            [243398.79,915448.17,69558.64],
            [69558.64,69558.64,266466.05]]

B_matrix = [[0,0,0],[0,0,0],[0,0,0]]

D_matrix = [[9809831.65,5726236.70,3249868.55],
            [5726236.70,8566403.68,3249868.55],
            [3249868.55,3249868.55,6063613.62]]




#___setting up the databank___
os.chdir("../..")
badir =  os. getcwd()  
os.chdir("03_FemResults")
femdir = os.getcwd()

cases = ['LC1','LC2','LC3',]
LC1dir ={}
LC2dir ={}
LC3dir ={}
maindir_panel_stability= {}
maindir_panel_stability ['LC1'] = LC1dir
maindir_panel_stability ['LC2'] = LC2dir
maindir_panel_stability ['LC3'] = LC3dir

for i in range (1,4):
    for j in range (1,6):
        maindir_panel_stability [f'LC{i}'] [f'Panel{j}'] = {}



#___get values for stabiliy___
file_path = os.path.join(femdir, f'{filename_stability_panels}.xlsx')
wb = load_workbook(file_path)
ws = wb[filename_stability_panels]


row = 6
column = 6

for LoadCases in maindir_panel_stability:
    for i in range (1,6):
        row += 6
        for j in range(0,6):
            id = {}
            id ['xx'] = ws.cell(row=row+j,column=column+0).value
            id ['xy'] = ws.cell(row=row+j,column=column+1).value
            id ['yy'] = ws.cell(row=row+j,column=column+2).value
            maindir_panel_stability [LoadCases] [f'Panel{i}'] [f'Element{j+1}'] = id


#___averaged values panels___
for LoadCases in maindir_panel_stability:
    for Panels in maindir_panel_stability[LoadCases]:
        xx = 0
        xy = 0
        yy = 0
        for Elements,values in maindir_panel_stability[LoadCases] [Panels].items():
            M = values ['xx']
            K = values ['xy']
            L = values ['yy']
            xx = xx + M
            xy = xy + K
            yy = yy + L
        maindir_panel_stability[LoadCases] [Panels] ['average_xx'] = xx/6
        maindir_panel_stability[LoadCases] [Panels] ['average_xy'] = xy/6
        maindir_panel_stability[LoadCases] [Panels] ['average_yy'] = yy/6

#___biax crit___
for LoadCases in maindir_panel_stability:
    for Panels in maindir_panel_stability[LoadCases]:
        sigma_x = maindir_panel_stability[LoadCases] [Panels] ['average_xx']
        sigma_y = maindir_panel_stability[LoadCases] [Panels] ['average_yy']
        tau_xy = maindir_panel_stability[LoadCases] [Panels] ['average_xy']

        beta = sigma_y/sigma_x
        alpha = a_width/b_length

        sigma_crit_biax = (np.pi**2/((b_length**2)*t_thikness))*(1/(((m_mave/alpha)**2)+(beta*(n_wave**2))))*(D_matrix[0][0] * ((m_wave/alpha)**4) + 2*(D_matrix[0][1]+D_matrix[2][2])*(((m_wave*n_wave)/alpha)**2) + (D_matrix[1][1] * (n_wave**4)))
        maindir_panel_stability[LoadCases] [Panels] ['sigma_crit_biax'] = sigma_crit_biax
        RF_biax = sigma_crit_biax/sigma_x

        epsilon = ((D_matrix[0][0]*D_matrix[1][1])**0.5)/(D_matrix[0][1]+2*D_matrix[2][2])
        if epsilon >= 1:
            tau_crit_biax = (4/(t_thikness*(b_length**2)))*(((D_matrix[0][0]*(D_matrix[1][1]**3))**0.25)*(8.12+(5.05/epsilon)))
        if epsilon < 1:
            tau_crit_biax = (4/(t_thikness*(b_length**2)))*(((D_matrix[1][1]*(D_matrix[0][1]+2*D_matrix[2][2]))**0.5)*(11.7+(0.532*epsilon)+(0.938*(epsilon**2))))
        maindir_panel_stability[LoadCases] [Panels] ['tau_crit_biax'] = tau_crit_biax
        RF_shear = tau_crit_biax/tau_xy
        RF_comb = 1/((1/RF_biax)+(1/RF_shear)**2)
        maindir_panel_stability[LoadCases] [Panels] ['RF_panel_buckel'] = RF_comb

print ('hey')