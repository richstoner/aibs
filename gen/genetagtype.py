# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GeneTagType(object):
    '''aibs.model.genetagtype (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.description = ''

    # Associations
    self.gene_tags = [] # has_many GeneTag

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here