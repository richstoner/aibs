# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GenomeLocus(object):
    '''aibs.model.genomelocus (autogen)'''

    # Fields
    self.id = 0
    self.start_pos = 0
    self.stop_pos = 0
    self.chromosome_id = 0
    self.reference_genome_id = 0
    self.parent_locus_id = 0
    self.genomic_feature_id = 0
    self.genomic_feature_type = ''

    # Associations
    self.chromosome = None # belongs_to Chromosome
    self.reference_genome = None # belongs_to ReferenceGenome
    self.parent_genome_locus = None # belongs_to GenomeLocus
    self.child_genome_loci = [] # has_many GenomeLocus

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here