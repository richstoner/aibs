# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GoExon(object):
    '''aibs.model.goexon (autogen)'''

    # Fields
    self.id = 0

    # Associations
    self.genome_locus = None # has_one GenomeLocus
    self.gene_association = None # has_one GeneAssociation

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here