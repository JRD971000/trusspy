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
        self.nodes = np.array([],dtype=object)
        #self.labels = np.array([],dtype=int)
        #self.coordinates = np.zeros((0,3),dtype=np.float)
        #self.Node = Node
        
    def __enter__(self):
        return self
    def __exit__(self, H_type, H_value, H_traceback):
        pass
        
    def add(self,N,*args, **kwargs):
        self.nodes = np.append(self.nodes,N)

    def build(self):
        self.labels = np.array([],dtype=int)
        self.coordinates = np.zeros((0,3),dtype=np.float)

        for N in self.nodes:
            self.coordinates = np.vstack((self.coordinates,N.coordinates))
            self.labels      = np.append(self.labels,N.label)
            
        self.fix()
        
        # remove in a further step
        self.coords = self.coordinates.copy()

    def add_nodes(self,NN):
        for N in NN:
            self.add_node(N)
            
    def fix(self):
        indices = np.argsort(self.labels)
        self.labels = self.labels.take(indices)
        self.coordinates = self.coordinates.take(indices,axis=0)