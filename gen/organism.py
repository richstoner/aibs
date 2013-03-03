# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Organism(object):
    '''aibs.model.organism (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.ncbitaxonomyid = 0
    self.tags = ''

    # Associations
    self.ontologies = [] # has_many Ontology
    self.ages = [] # has_many Age
    self.chromosomes = [] # has_many Chromosome
    self.donors = [] # has_many Donor
    self.genes = [] # has_many Gene
    self.reference_genomes = [] # has_many ReferenceGenome
    self.reference_spaces = [] # has_many ReferenceSpace

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here