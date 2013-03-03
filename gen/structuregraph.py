# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class StructureGraph(object):
    '''aibs.model.structuregraph (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.root_structure_id = 0
    self.ontology_id = 0

    # Associations
    self.root_structure = None # belongs_to Structure
    self.ontology = None # belongs_to Ontology
    self.atlases = [] # has_many Atlas
    self.atlas_infos = [] # has_many AtlasInfo
    self.ontology_nodes = [] # has_many OntologyNode

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here