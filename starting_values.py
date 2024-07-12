######################################################################################################################
E_11 = 135369.47 * 0.9  #MPa
E_22 = 10413.04 * 0.9  #MPa
G_12 = 5206.52 * 0.9  #MPa        

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


filename_strength_panels_x = 'X_Ply'
filename_strength_panels_y = 'Y_Ply'
filename_strength_panels_xy = 'XY_Ply'

filename_stability_panels = '2D_3D'

filename_stringer_stability = 'Axial_Stress'
######################################################################################################################