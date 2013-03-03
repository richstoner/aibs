# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GeneAssociation(object):
    '''aibs.model.geneassociation (autogen)'''

    # Fields
    self.id = 0
    self.gene_feature_id = 0
    self.gene_feature_type = ''
    self.gene_id = 0
    self.gene_association_source_id = 0

    # Associations
    self.gene = None # belongs_to Gene
    self.gene_association_source = None # belongs_to GeneAssociationSource

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here