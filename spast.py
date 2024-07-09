from openpyxl import load_workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.styles import Alignment
from openpyxl.utils import column_index_from_string,get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import logging
import os



######################################################################################################################

filename_stability_panels = 'stability_panels'
######################################################################################################################



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



print ('hey')