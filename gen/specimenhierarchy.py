# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class SpecimenHierarchy(object):
    '''aibs.model.specimenhierarchy (autogen)'''

    # Fields
    self.ancestor_id = 0
    self.descendant_id = 0
    self.generations = 0

    # Associations
    self.ancestor = None # belongs_to Specimen
    self.descendant = None # belongs_to Specimen

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here