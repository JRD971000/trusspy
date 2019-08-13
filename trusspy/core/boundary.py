# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:48:03 2018

@author: adutz
"""

import numpy as np

class BoundaryU:
    """Mechanical (displacement) node based boundary class.
    
    Parameter
    ---------
    node : int
        Node ID number
    values : array_like
        List of boundary components: `[U1, U2, U3]`. 
        Set 1 for active (free) DOF and 0 for inactive (locked) DOF.
        
    Attributes
    ----------
    node : int
        Node ID number
    dof : ndarray
        Array of boundary components: `array([U1, U2, U3])`. 
        Set 1 for active (free) DOF and 0 for inactive (locked) DOF.

    """
    def __init__(self,node,dof):
        self.node = node
        self.dof = np.array(dof)