# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GeneAssociationSource(object):
    '''aibs.model.geneassociationsource (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.description = ''

    # Associations
    self.gene_associations = [] # has_many GeneAssociation

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here