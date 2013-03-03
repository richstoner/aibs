# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class NeuroNameStructureSynonym(object):
    '''aibs.model.neuronamestructuresynonym (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.language = ''
    self.organism = ''
    self.concept_id = 0
    self.default_name = ''
    self.old_concept_type = ''
    self.old_nn_id = 0

    # Associations

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here