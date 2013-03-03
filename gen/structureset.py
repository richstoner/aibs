# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class StructureSet(object):
    '''aibs.model.structureset (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.description = ''

    # Associations
    self.structure_sets_structures = [] # has_many StructureSetsStructure
    self.structures = [] # has_many Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here