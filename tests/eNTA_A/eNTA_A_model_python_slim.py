# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:06 2018

@author: adutz
"""

# Example NTA (A)
# ---------------
# - 3D truss system
# - material: linear elastic

# import TrussPy
import trusspy as tp

M = tp.Model(logfile=False)

with M.NodeHandler as MN:
    MN.add( tp.Node(1, coordinates=( 2.5 , 0   , 0  ) ))
    MN.add( tp.Node(2, coordinates=(-1.25, 1.25, 0  ) ))
    MN.add( tp.Node(3, coordinates=( 1   , 2   , 0  ) ))
    MN.add( tp.Node(4, coordinates=(-0.5 , 1.5 , 1.5) ))
    MN.add( tp.Node(5, coordinates=(-2.5 , 4.5 , 2.5) ))
    
g1 = tp.Geometry( classification=1, properties=[0.50])
g2 = tp.Geometry( classification=1, properties=[0.75])
g3 = tp.Geometry( classification=1, properties=[1.00])

m1 = tp.Material( classification=1, properties=[1.0])

with M.ElementHandler as ME:
    ME.add( tp.Element(1, connectivity=(1,4), material=m1, geometry=g2 ))
    ME.add( tp.Element(2, connectivity=(2,4), material=m1, geometry=g3 ))
    ME.add( tp.Element(3, connectivity=(3,4), material=m1, geometry=g1 ))
    ME.add( tp.Element(4, connectivity=(3,5), material=m1, geometry=g2 ))
    ME.add( tp.Element(5, connectivity=(2,5), material=m1, geometry=g3 ))
    ME.add( tp.Element(6, connectivity=(4,5), material=m1, geometry=g3 ))
    
with M.BoundaryHandler as MB:
    #MB.add( tp.Boundary(1, dof=(0,0,0) ))
    #MB.add( tp.Boundary(2, dof=(0,0,0) ))
    MB.add( tp.Boundary(4, dof=(1,1,1) ))
    MB.add( tp.Boundary(5, dof=(1,0,1) ))
    
with M.ExternalForceHandler as MF:
    MF.add( tp.Force(4, components=( 1, 1,-1) ))
    MF.add( tp.Force(5, components=(-2, 0,-2) ))

M.Settings.dlpf = 0.005
M.Settings.du = 0.05

M.Settings.incs = 100
M.Settings.stepcontrol = True
M.Settings.maxfac = 4

M.Settings.ftol = 8
M.Settings.xtol = 8
M.Settings.nfev = 8

M.Settings.dxtol = 1.25

## lim_scale < 1: fixed value for all axis (good for videos)
## lim_scale > 1: scale factor for min/max values
## forces:        1 N = "force_scale" L

## Create Model, Run, show Results
M.build()
M.run()

## model plot: undeformed and deformed configuration for last increment
fig, ax = M.plot_model(config=['undeformed'],
             view='3d',
             contour='force',
             lim_scale=(-3,2,0,5,-1,4),
             force_scale=5.0,
             inc=0)
#fig.savefig('model_undeformed_inc0_3d.pdf')
#fig.savefig('model_undeformed_inc0_3d.png')

#fig, ax = M.plot_model(config=['undeformed'],
#             view='xz',
#             contour='force',
#             lim_scale=1.4,
#             force_scale=2.0,
#             inc=0)
#fig.savefig('model_undeformed_inc0_xz.pdf')
#fig.savefig('model_undeformed_inc0_xz.png')
#
#fig, ax = M.plot_model(config=['undeformed'],
#             view='yz',
#             contour='force',
#             lim_scale=1.4,
#             force_scale=2.0,
#             inc=0)
#fig.savefig('model_undeformed_inc0_yz.pdf')
#fig.savefig('model_undeformed_inc0_yz.png')
#
#fig, ax = M.plot_model(config=['undeformed'],
#             view='xy',
#             contour='force',
#             lim_scale=1.4,
#             force_scale=2.0,
#             inc=0)
#fig.savefig('model_undeformed_inc0_xy.pdf')
#fig.savefig('model_undeformed_inc0_xy.png')
#
pinc = 12 #105
fig, ax = M.plot_model(config=['deformed'],
             view='xz',
             contour='force',
             #lim_scale=(-4,4,-2,6,-1,5),
             lim_scale=1.3,
             force_scale=500.0,
             inc=pinc)
#fig.savefig('model_contour-force_inc40_xz.pdf')
#fig.savefig('model_contour-force_inc40_xz.png')
#
#fig, ax = M.plot_model(config=['deformed'],
#             view='yz',
#             contour='force',
#             #lim_scale=(-4,4,-2,6,-1,5),
#             lim_scale=1.3,
#             force_scale=500.0,
#             inc=pinc)
#fig.savefig('model_contour-force_inc40_yz.pdf')
#fig.savefig('model_contour-force_inc40_yz.png')
#
#fig, ax = M.plot_model(config=['deformed'],
#             view='xy',
#             contour='force',
#             #lim_scale=(-4,4,-2,6,-1,5),
#             lim_scale=1.3,
#             force_scale=500.0,
#             inc=pinc)
#fig.savefig('model_contour-force_inc40_xy.pdf')
#fig.savefig('model_contour-force_inc40_xy.png')
#
#fig, ax = M.plot_model(config=['deformed'],
#             view='3d',
#             contour='force',
#             lim_scale=(-3,2,0,5,-2,1),
#             #lim_scale=1.2,
#             force_scale=500.0,
#             inc=pinc)
#fig.savefig('model_contour-force_inc40_3d.pdf')
#fig.savefig('model_contour-force_inc40_3d.png')
#
#M.plot_movie(config=['deformed'],
#             view='3d',
#             contour='force',
#             lim_scale=(-3,2,0,5,-1,4), #3D
#             #lim_scale=-5, #XZ
#             #lim_scale=(-4,4,-2,6), #XY
#             #lim_scale=(-2,6,-2,6), #YZ
#             cbar_limits=[-0.3,0.3],
#             force_scale=50.0,
#             incs=range(0,M.Settings.incs,1))
##
### history plot
#Disp = 'Displacement X'
#fig,ax = M.plot_history(nodes=[4,4],X=Disp,Y='LPF')
#fig,ax = M.plot_history(nodes=[5,5],X=Disp,Y='LPF',fig=fig,ax=ax)
#fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.pdf')
#fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.png')
#
#Disp = 'Displacement Y'
#fig,ax = M.plot_history(nodes=[4,4],X=Disp,Y='LPF')
##fig,ax = M.plot_history(nodes=[5,5],X=Disp,Y='LPF',fig=fig,ax=ax)
#fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.pdf')
#fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.png')
#
Disp = 'Displacement Z'
fig,ax = M.plot_history(nodes=[4,4],X=Disp,Y='LPF')
fig,ax = M.plot_history(nodes=[5,5],X=Disp,Y='LPF',fig=fig,ax=ax)
#fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.pdf')
#fig.savefig('history_node45_Disp'+Disp[-1]+'-LPF.png')
##
### show plots
##M.plot_show()