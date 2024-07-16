######################################################################################################################

person = 'Niki' 

E_11_pers = {'Noah':135369.47,
             'Niki':135375.58}

E_22_pers = {'Noah':10413.04,
             'Niki':10413.51}

G_pers = {'Noah':5206.52,
          'Niki':5206.75}

E_11 = E_11_pers[person] * 0.9  #MPa
E_22 = E_22_pers[person] * 0.9  #MPa
G_12 = G_pers[person] * 0.9  #MPa    


v_12 = 0.33
v_21 = (v_12 * E_22)/E_11

R_paralel_t = 3050  #MPa
R_paralel_c = 1500  #MPa
R_perpendicular_t = 300  #MPa
R_perpendicular_c = 50   #MPa
R_shear = 100 #MPa

p_weird = 0.25

a_width = 600 #m
b_length = 400 #m
t_thikness = 1.104*8

stringer_thikness = 2.944 #mm
stringer_dim_1 = 70 #mm
stringer_dim_2 = 40 #mm

sigma_ult = 650 #MPa


m_wave = 2
n_wave = 1

result_file = f'result_2_1_{person}'

filename_strength_panels_x = f'X_Ply_{person}'
filename_strength_panels_y = f'Y_Ply_{person}'
filename_strength_panels_xy = f'XY_Ply_{person}'

filename_stability_panels = f'2D_3D_{person}'

filename_stringer_stability = f'1D_Stress_{person}'
filename_strength_stringer = f'1D_Strain_{person}'




A_matrix_stringer = {'Noah':[[172517.98,54088.62,0.00],
                     [54088.62,172517.98,0.00],
                     [0.00,0.00,59214.68]],
                     'Niki':[[172525.76,54091.07,0.00],
                     [54091.07,172525.76,0.00],
                     [0.00,	0.00,59217.34]]}

D_matrix_stringer = {'Noah':[[113389.70,62839.36,18839.82],
                     [62839.36, 88269.94, 18839.82],
                     [18839.82, 18839.82, 66541.71]],
                     'Niki':[[113394.81,62842.21,18840.67],
                     [62842.21,88273.92,18840.67],
                     [18840.67,18840.67,66544.72]]}

A_matrix_panel = {'Noah':[[517553.93, 162265.86, 0.00],
                  [162265.86, 517553.93, 0.00],
                  [0.00,	0.00,	177644.03]],
                  'Niki':[[517577.27,162273.21,0.00],
                  [162273.21,517577.27,0.00],
                  [0.00,0.00,177652.03]]}

D_matrix_panel = {'Noah':[[3061521.95,1696662.73,508675.08],
                  [1696662.73,2383288.51,508675.08],
                  [508675.08,508675.08,1796626.26]],
                  'Niki':[[3061659.88,1696739.56,508698.04],
                  [1696739.56,2383395.84,508698.04],
                  [508698.04,508698.04,1796707.31]]}
######################################################################################################################