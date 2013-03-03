# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GeneTag(object):
    '''aibs.model.genetag (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.created_at = None
    self.updated_at = None
    self.gene_tag_type_id = 0

    # Associations
    self.genes = [] # has_and_belongs_to_many Gene
    self.gene_tag_type = None # belongs_to GeneTagType

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here