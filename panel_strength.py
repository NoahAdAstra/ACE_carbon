from openpyxl import load_workbook
import numpy as np
import os

#___setting up the data base__

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
file_path = os.path.join(femdir, f'{filename_strength_panels_x}.xlsx')
wb = load_workbook(file_path)
ws = wb[filename_strength_panels_x]


column = 6
row = -228
for LoadCases in maindir_panel_strength:
    row += 240
    for j in range(0,8): 
        id = {}
        id ['sigma_x'] = ws.cell(row=row+j*30,column=column).value
        maindir_panel_strength [LoadCases] [f'Ply{j+1}'] = id


#___ply Y___         
file_path = os.path.join(femdir, f'{filename_strength_panels_y}.xlsx')
wb = load_workbook(file_path)
ws = wb[filename_strength_panels_y]

column = 6
row = -228
for LoadCases in maindir_panel_strength:
    row += 240
    for j in range(0,8): 
        hey = ws.cell(row=row+j*30,column=column).value
        maindir_panel_strength [LoadCases] [f'Ply{j+1}'].update({'sigma_y': hey})

#___ply XY___         
file_path = os.path.join(femdir, f'{filename_strength_panels_xy}.xlsx')
wb = load_workbook(file_path)
ws = wb[filename_strength_panels_xy]

column = 6
row = -228
for LoadCases in maindir_panel_strength:
    row += 240
    for j in range(0,8): 
        hey = ws.cell(row=row+j*30,column=column).value
        maindir_panel_strength [LoadCases] [f'Ply{j+1}'].update({'sigma_xy': hey})

#___FF RF and IFF RF