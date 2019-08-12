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
        
        # Node-based displacement boundary condition
        self.Unodes = None
        
        # UValue:
        # 1=active    (free)  DOF
        # 0=inactive (locked) DOF
        self.Uvalues = None
        
        # NOT IMPLEMENTED
        # Element based thermal boundary condition
        #self.Telements = None
        #self.Tvalues = None
        
    def __enter__(self):
        return self
    def __exit__(self, H_type, H_value, H_traceback):
        pass
        
    def add(self,B, *args, **kwargs):
        """add displacement boundary"""
            
        if self.Unodes is None:
            self.Unodes = np.array([B.node])
            self.Uvalues = np.array(B.values)
        else:
            self.Unodes = np.append(self.Unodes,B.node)
            self.Uvalues = np.vstack((self.Uvalues,B.values))
            
    def add_bounds_U(self,BB):
        """add list of displacement boundaries"""
        for B in BB:
            self.add_bound_U(B)
            
    def fix_bounds_U(self,nodelist):
        # check for undefined DOF --> set them all to free
        
        # are nodelist entries in Unodes?
        mask = np.isin(nodelist, self.Unodes, invert=True)
        fix_nodes = nodelist[mask] # nodes to fix
        for n in fix_nodes:
            B = BoundaryU(n, (1,1,1))
            self.add(B)
        indices = np.argsort(self.Unodes)
        self.Unodes = self.Unodes.take(indices)
        self.Uvalues = self.Uvalues.take(indices,axis=0)
                             
    def add_bound_T(self,B):
        # add thermal boundary
        if self.Tnodes is None:
            self.Tnodes = np.array([B.node])
            self.Tvalues = np.array(B.value)
        else:
            self.Tnodes = np.append(self.Tnodes,B.node)
            self.Tvalues = np.vstack((self.Tvalues,B.value))
            
    def add_bounds_T(self,BB):
        # add list of thermal boundaries
        for B in BB:
            self.add_bound_T(B)