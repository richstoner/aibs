# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Chromosome(object):
    '''aibs.model.chromosome (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.organism_id = 0

    # Associations
    self.organism = None # belongs_to Organism
    self.genes = [] # has_many Gene
    self.genome_locuses = [] # has_many GenomeLocus

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here