# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class StructureCenter(object):
    '''aibs.model.structurecenter (autogen)'''

    # Fields
    self.id = 0
    self.structure_id = 0
    self.x = 0
    self.y = 0
    self.z = 0
    self.reference_space_id = 0

    # Associations
    self.structure = None # belongs_to Structure
    self.reference_space = None # belongs_to ReferenceSpace

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here