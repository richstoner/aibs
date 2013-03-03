# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GeneClassificationCount(object):
    '''aibs.model.geneclassificationcount (autogen)'''

    # Fields
    self.id = 0
    self.product_id = 0
    self.gene_classification_id = 0
    self.distinct_gene_count = 0

    # Associations
    self.gene_classification = None # belongs_to GeneClassification
    self.genes = [] # has_many Gene
    self.product = None # belongs_to Product

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here