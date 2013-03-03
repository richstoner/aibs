# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GeneLookup(object):
    '''aibs.model.genelookup (autogen)'''

    # Fields
    self.id = 0
    self.term = ''
    self.termtype = ''
    self.gene_id = 0
    self.product_id = 0

    # Associations
    self.gene = None # belongs_to Gene
    self.product = None # belongs_to Product

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here