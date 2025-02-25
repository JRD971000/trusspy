# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:06 2018

@author: adutz
"""

# Example NTA (A)
# ---------------
# - 3D truss system
# - material: linear elastic

# import TrussPy (absolute path to local copy if trusspy not installed)
try:
    import trusspy as tp
except ImportError:
    import sys
    sys.path.append(r'../../')
    import trusspy as tp

M = tp.Model('eNTA_X_input.xlsx', logfile=True)

M.Settings.dlpf = 0.005
M.Settings.du = 0.05

M.Settings.incs = 180

M.Settings.stepcontrol = True
M.Settings.maxfac = 1

M.Settings.ftol = 8
M.Settings.xtol = 8
M.Settings.nfev = 8

M.Settings.dxtol = 1.25

# lim_scale < 1: fixed value for all axis (good for videos)
# lim_scale > 1: scale factor for min/max values
# forces:        1 N = "force_scale" L

# Create Model, Run, show Results
M.build()
M.run()

# model plot: undeformed and deformed configuration for last increment
fig, ax = M.plot_model(config=['undeformed','deformed'],
             view='xz',
             contour='force',
             lim_scale=2,
             force_scale=0.2,
             inc=-1)
fig.savefig('model_contour-force_inc-last.pdf')

#M.plot_movie(config=['undeformed','deformed'],
#             view='xz',
#             contour='stretch',
#             lim_scale=-1.5,
#             force_scale=10.0,
#             incs='all')

# history plot
Disp = 'Displacement X'
fig,ax = M.plot_history(nodes=[4,4],X=Disp,Y='LPF')
fig,ax = M.plot_history(nodes=[5,5],X=Disp,Y='LPF',fig=fig,ax=ax)
fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.pdf')

Disp = 'Displacement Y'
fig,ax = M.plot_history(nodes=[4,4],X=Disp,Y='LPF')
fig,ax = M.plot_history(nodes=[5,5],X=Disp,Y='LPF',fig=fig,ax=ax)
fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.pdf')

Disp = 'Displacement Z'
fig,ax = M.plot_history(nodes=[4,4],X=Disp,Y='LPF')
fig,ax = M.plot_history(nodes=[5,5],X=Disp,Y='LPF',fig=fig,ax=ax)
fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.pdf')

# show plots
#M.plot_show()