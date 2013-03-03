# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Product(object):
    '''aibs.model.product (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.abbreviation = ''
    self.resource = ''
    self.description = ''
    self.documentation = ''
    self.tags = ''
    self.species = ''

    # Associations
    self.ontologies = [] # has_and_belongs_to_many Ontology
    self.data_sets = [] # has_and_belongs_to_many DataSet
    self.donors = [] # has_and_belongs_to_many Donor
    self.genes = [] # has_and_belongs_to_many Gene
    self.probes = [] # has_and_belongs_to_many Probe
    self.reference_spaces = [] # has_and_belongs_to_many ReferenceSpace
    self.data_points = [] # has_many DataPoint
    self.documents = [] # has_many Document

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here