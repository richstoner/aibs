# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class MolbioAuthority(object):
    '''aibs.model.molbioauthority (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.description = ''
    self.gene_type_class = ''

    # Associations
    self.transcripts = [] # has_many Transcript
    self.gene_associations = [] # has_many GeneAssociation
    self.genes = [] # has_many Gene

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here