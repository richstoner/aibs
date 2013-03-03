# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class StructureHierarchy(object):
    '''aibs.model.structurehierarchy (autogen)'''

    # Fields
    self.ancestor_id = 0
    self.descendant_id = 0
    self.generations = 0

    # Associations
    self.ancestor = None # belongs_to Structure
    self.descendant = None # belongs_to Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here