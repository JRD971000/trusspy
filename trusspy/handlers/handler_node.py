# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:46:59 2018

@author: adutz
"""

import numpy as np
from ..core.node import Node

class NodeHandler:
    "Handler for Nodes"
    def __init__(self):
        self.labels = np.array([],dtype=int)
        self.coords = np.zeros((0,3))
        #self.Node = Node
        
    def __enter__(self):
        return self
    def __exit__(self, H_type, H_value, H_traceback):
        pass
        
    def add(self,N,*args, **kwargs):

        self.labels = np.append(self.labels,N.label)
        self.coords = np.vstack((self.coords,N.coordinates))

    def add_nodes(self,NN):
        for N in NN:
            self.add_node(N)
            
    def fix_nodes(self):
        indices = np.argsort(self.labels)
        self.labels = self.labels.take(indices)
        self.coords = self.coords.take(indices,axis=0)