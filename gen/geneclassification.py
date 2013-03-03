# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GeneClassification(object):
    '''aibs.model.geneclassification (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.source = ''
    self.category = ''
    self.use = ''

    # Associations
    self.genes = [] # has_and_belongs_to_many Gene
    self.gene_classification_counts = [] # has_many GeneClassificationCount

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here