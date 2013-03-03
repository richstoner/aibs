# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class StructureLookup(object):
    '''aibs.model.structurelookup (autogen)'''

    # Fields
    self.id = 0
    self.term = ''
    self.termtype = ''
    self.structure_id = 0
    self.ontology_id = 0

    # Associations
    self.structure = None # belongs_to Structure
    self.ontology = None # belongs_to Ontology

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here