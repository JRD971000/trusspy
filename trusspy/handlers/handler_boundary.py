# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:48:42 2018

@author: adutz
"""

import numpy as np
from ..core.boundary import BoundaryU

class BoundaryHandler:
    "Handler for Boundary Conditions"
    def __init__(self):
        self.boundaries = np.array([],dtype=object)
        
    def __enter__(self):
        return self
    def __exit__(self, H_type, H_value, H_traceback):
        pass
        
    def add(self,B, *args, **kwargs):
        """add displacement boundary"""
        
        self.boundaries = np.append(self.boundaries,B)
            
    def build(self,reset=True):
        self.nodes = np.array([],dtype=int)
        self.dof = np.zeros((0,3),dtype=np.float)

        for B in self.boundaries:
            self.nodes      = np.append(self.nodes,B.node)
            self.dof = np.vstack((self.dof,B.dof))
            
    def add_list(self,BB):
        """add list of displacement boundaries"""
        for B in BB:
            self.add(B)
            
    def fix(self,nodelist):
        # check for missing external forces --> set them all to zero
        
        # are nodelist entries in force-nodes?
        mask = np.isin(nodelist, self.nodes, invert=True)
        fix_nodes = nodelist[mask] # nodes to fix

        #comp = self.components.shape[1]
        for n in fix_nodes:
            #F = ExternalForce(n, np.zeros(comp))
            B = BoundaryU(n, (0,0,0))
            self.add(B)
            
        # re-build nodes and components
        self.build()
        
        indices = np.argsort(self.nodes)
        self.nodes = self.nodes.take(indices)
        self.dof = self.dof.take(indices,axis=0)