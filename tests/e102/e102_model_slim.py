# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:29:06 2018

@author: adutz
"""

# Example 102
# -----------
# - 2 Trusses with 1 DOF
# - material: linear elastic

# import TrussPy
import trusspy as tp

M = tp.Model(logfile=False)

with M.NodeHandler as MN:
    MN.add( tp.Node(1, coordinates=( 0, 0, 0)))
    MN.add( tp.Node(2, coordinates=( 1, 0, 1)))
    MN.add( tp.Node(3, coordinates=( 2, 0, 0)))
    
geo1 = tp.Geometry( classification=1, properties=[1])
mat1 = tp.Material( classification=1, properties=[1])

with M.ElementHandler as ME:
    ME.add( tp.Element(1, connectivity=(1,2), material=mat1, geometry=geo1))
    ME.add( tp.Element(2 ,connectivity=(2,3), material=mat1, geometry=geo1))
#    
with M.BoundaryHandler as MB:
    MB.add( tp.Boundary(1, (0,0,0) ))
    MB.add( tp.Boundary(2, (0,0,1) ))
    MB.add( tp.Boundary(3, (0,0,0) ))
#    
with M.ExternalForceHandler as MF:
    MF.add( tp.Force(2, ( 0, 0,-1) ))
#
M.Settings.incs = 100
M.Settings.xlimit = (2,0.5)

M.Settings.stepcontrol = True
M.Settings.maxfac = 4
#
## Create Model, Run, show Results
M.build()
M.run()
#
#fig, ax = M.plot_model(config=['undeformed'],inc=0)
#fig.savefig('model_undeformed.png')
#fig.savefig('model_undeformed.pdf')
#
## model plot: undeformed and deformed configuration for last increment
fig, ax = M.plot_model(config=['deformed'],inc=-1,
                       view='xz',
                       contour='force',
                       lim_scale=(-1,3,-2.5,1.5)
                      )
#fig.savefig('model_deformed.png')
#fig.savefig('model_deformed.pdf')
#
## history plot
fig, ax = M.plot_history(nodes=[2,2],X='Displacement Z',Y='LPF')
#
## re-run with plasticity
#with M.Elements as ME:
#    K = 0.1   # plastic modulus
#    Sy = 0.1  # initial yield stress
#    
#    ME.assign_mtype(    'all',  2   )
#    ME.assign_material( 'all', [E, K, Sy])
#    
## Create Model, Run, show Results
#M.build()
#M.run()
#    
#fig, ax = M.plot_history(nodes=[2,2],X='Displacement Z',Y='LPF',fig=fig,ax=ax)
#ax.legend(['Node 2: linear elastic','Node 2: elastic-plastic (isotropic hardening)'])
#fig.savefig('history_node2_DispZ-LPF.png')
#fig.savefig('history_node2_DispZ-LPF.pdf')