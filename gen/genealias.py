# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GeneAlias(object):
    '''aibs.model.genealias (autogen)'''

    # Fields
    self.id = 0
    self.gene_id = 0
    self.acronym = ''

    # Associations
    self.gene = None # belongs_to Gene

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here