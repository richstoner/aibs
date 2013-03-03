# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class HomologousGeneAssociation(object):
    '''aibs.model.homologousgeneassociation (autogen)'''

    # Fields
    self.id = 0
    self.gene_id = 0
    self.homologous_gene_id = 0
    self.source = ''

    # Associations
    self.homologous_gene = None # belongs_to Gene
    self.gene = None # belongs_to Gene

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here