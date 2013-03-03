# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class StructureSetsStructure(object):
    '''aibs.model.structuresetsstructure (autogen)'''

    # Fields
    self.structure_set_id = 0
    self.structure_id = 0
    self.id = 0
    self.structure_order = 0

    # Associations
    self.structure = None # belongs_to Structure
    self.structure_set = None # belongs_to StructureSet

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here