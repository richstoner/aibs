# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class OntologyNode(object):
    '''aibs.model.ontologynode (autogen)'''

    # Fields
    self.id = 0
    self.depth = 0
    self.st_order = 0
    self.structure_id_path = []
    self.acronym_path = []
    self.color = ''
    self.acronym = ''
    self.name = ''
    self.structure_graph_id = 0
    self.structure_id = 0

    # Associations
    self.structure_graph = None # belongs_to StructureGraph
    self.structure = None # belongs_to Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here