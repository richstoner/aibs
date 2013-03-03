# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class ReferenceToReferenceTransform(object):
    '''aibs.model.referencetoreferencetransform (autogen)'''

    # Fields
    self.id = 0
    self.from_reference_space_id = 0
    self.to_reference_space_id = 0
    self.t_00 = 0.0
    self.t_01 = 0.0
    self.t_02 = 0.0
    self.t_03 = 0.0
    self.t_04 = 0.0
    self.t_05 = 0.0
    self.t_06 = 0.0
    self.t_07 = 0.0
    self.t_08 = 0.0
    self.t_09 = 0.0
    self.t_10 = 0.0
    self.t_11 = 0.0

    # Associations
    self.from_reference_space = None # belongs_to ReferenceSpace
    self.to_reference_space = None # belongs_to ReferenceSpace

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here