# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:04:51 2019

@author: adutz
"""

import numpy as np

class Geometry:
    
    def __init__(self, classification=1, properties=[np.nan]):
        self.classification = classification
        self.properties = properties