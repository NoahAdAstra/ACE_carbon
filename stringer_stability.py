from openpyxl import load_workbook
import numpy as np
import os
import starting_values as val

maindir_stringer_stability= {} 
for i in range (1,4):
    maindir_stringer_stability.update({f'LC{i}':{}})
    for j in range (1,6):
        maindir_stringer_stability [f'LC{i}'].update({f'Stringer{j}':{}}) 
        

b_top = val.stringer_dim_1/2
sigma_crip_top = (1.63/((b_top/val.stringer_thikness)**0.717)) * val.sigma_ult

b_bottom = val.stringer_dim_2
sigma_crip_bottom = (1.63/((b_bottom/val.stringer_thikness)**0.717)) * val.sigma_ult

sigma_crip_stringer = (sigma_crip_top*b_top*val.stringer_thikness*2 + sigma_crip_bottom*b_bottom*val.stringer_thikness)/(b_top*val.stringer_thikness*2 + b_bottom*val.stringer_thikness)

for LoadCases in maindir_stringer_stability:
    for Stringer in maindir_stringer_stability[LoadCases]: 
        RF_crip = sigma_crip_stringer/sigma_comb
        maindir_stringer_stability[LoadCases] [Stringer].update({'RF_crip':RF_crip})