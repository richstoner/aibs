# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class RnaseqDesign(object):
    '''aibs.model.rnaseqdesign (autogen)'''

    # Fields
    self.id = 0
    self.name = ''

    # Associations
    self.rnaseq_gene_data_sets = [] # has_many RnaseqGeneDataSet
    self.genes = [] # has_and_belongs_to_many Gene

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here