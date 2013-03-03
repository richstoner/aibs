# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Ontology(object):
    '''aibs.model.ontology (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.organism_id = 0
    self.has_atlas = None
    self.description = ''
    self.abbreviation = ''

    # Associations
    self.structure_graphs = [] # has_many StructureGraph
    self.structure_lookups = [] # has_many StructureLookup
    self.structures = [] # has_many Structure
    self.organism = None # belongs_to Organism
    self.products = [] # has_and_belongs_to_many Product

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here