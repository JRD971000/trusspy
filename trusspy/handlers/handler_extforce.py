# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:49:34 2018

@author: adutz
"""

import numpy as np
from ..core.external_force import ExternalForce

class ExternalForceHandler:
    "Handler for External Forces"
    def __init__(self):
        self.forces = np.array([],dtype=object)
        
        #self.nodes = np.array([],dtype=int)
        #self.components = np.zeros((0,3),dtype=np.float)
        
    def __enter__(self):
        return self
    def __exit__(self, H_type, H_value, H_traceback):
        pass
        
    def add(self,F, *args, **kwargs):
        self.forces = np.append(self.forces,F)
            
    def build(self):
        self.nodes = np.array([],dtype=int)
        self.components = np.zeros((0,3),dtype=np.float)

        for F in self.forces:
            self.nodes      = np.append(self.nodes,F.node)
            self.components = np.vstack((self.components,F.components))
            
    def add_forces(self,FF):
        
        for F in FF:
            self.add_force(F)
        
    def fix_forces(self,nodelist):
        # check for missing external forces --> set them all to zero
        
        # are nodelist entries in force-nodes?
        mask = np.isin(nodelist, self.nodes, invert=True)
        fix_nodes = nodelist[mask] # nodes to fix
        #comp = self.components.shape[1]
        for n in fix_nodes:
            #F = ExternalForce(n, np.zeros(comp))
            F = ExternalForce(n, (0,0,0))
            self.add(F)
        indices = np.argsort(self.nodes)
        self.nodes = self.nodes.take(indices)
        self.components = self.components.take(indices,axis=0)