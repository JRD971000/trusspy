# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:47:45 2018

@author: adutz
"""

import numpy as np
from ..core.element import Element
from ..core.material import Material
from ..core.geometry import Geometry

class ElementHandler:
    "Handler for Elements"
    def __init__(self):
        self.elements = np.array([],dtype=object)
        self.labels = np.array([],dtype=int)
        self.connectivities = np.zeros((0,2),dtype=int)
        self.classifications = np.array([],dtype=int)
        self.materials = np.array([],dtype=int)
        #self.Element = Element
        
    def __enter__(self):
        return self
    def __exit__(self, H_type, H_value, H_traceback):
        pass
    
    def build(self):
        self.connectivities = np.zeros((0,2),dtype=int)
        self.labels = np.array([],dtype=int)
        self.classifications = np.array([],dtype=int)
        self.materials = np.array([],dtype=int)
        for E in self.elements:
            print(E.classification)
            self.connectivities   = np.vstack((self.connectivities, 
                                                  E.connectivity))
            self.labels          = np.append(self.labels, 
                                                E.label)
            self.classifications = np.append(self.classifications, 
                                                E.classification)
            self.materials       = np.append(self.materials, 
                                                E.material.classification)
        
    def add(self,E,*args,**kwargs):
        "add single element to ElementManager"
        
        self.elements = np.append(self.elements,E)
    
    def del_element(self,label):
        idx = np.where(self.labels == label)[0]
        self.labels = np.delete(self.labels, idx,axis=0)
   
    def add_elements(self,EE):
        "add several elements from element list to ElementManager"
        for E in EE:
            self.add_element(E)

    def get_nodes(self,label):
        "choose element label and return connected end node"
        return self.conns[np.where(self.labels == label)][0]