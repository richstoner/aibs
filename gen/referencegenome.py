# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class ReferenceGenome(object):
    '''aibs.model.referencegenome (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.build = ''
    self.organism_id = 0

    # Associations
    self.organism = None # belongs_to Organism
    self.genome_locuses = [] # has_many GenomeLocus

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here