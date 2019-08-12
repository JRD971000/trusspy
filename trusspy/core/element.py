# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:46:06 2018

@author: adutz
"""

import numpy as np

class Element:
    """Element class.
    
    Parameter
    ---------
    label : int
        Element ID number
    conn : array_like
        List of Element connectivity : `[Node 1, Node 2]`
        
    elem_type : int, optional
        Element Type. (default is 1 for truss)
    mat_type : int, optional
        Material Type. (default is 1 for linear-elastic)
    material_properties : array_like, optional
        List with material parameters, 
        e.g. [Young's modulus, Thermal expansion coefficient] (default is [])
    geometric_properties : array_like, optional
        List with geometric parameters, 
        e.g. [Section area] (default is [])
        
    Attributes
    ----------
    label : int
        Element ID number
    connectivity : ndarray
        Array containing Element connectivity : `[Node 1, Node 2]`
    classification : int, optional
        Element Type. (default is 1 for truss)
    material : int, optional
        Material Type. (default is 1 for linear-elastic)
    #material_properties : array_like, optional
    #    List with material parameters, 
    #    e.g. [Young's modulus, Thermal expansion coefficient] (default is [])
    geometry : array_like, optional
        List with geometric parameters, 
        e.g. [Section area] (default is [])
        
    Todo
    ----
    + DONE rewrite material parameter storage
    + DONE material properties: type, mechanical and thermal parameter
    + DONE geometric porperties: section area
    """
    
    def __init__(self,label,connectivity,classification=1,
                 material=None,geometry=None):
        
        self.label = label
        self.connectivity = np.array(connectivity)
        self.classification = classification
        self.material = material
        self.geometry = geometry
        
    #def get_NE(self):
    #    """get end node of element"""
    #    return self.conn[1]
    
    #def get_NA(self):
    #    """get begin node of element"""
    #    return self.conn[0]