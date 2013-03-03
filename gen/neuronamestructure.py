# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class NeuroNameStructure(object):
    '''aibs.model.neuronamestructure (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.latin_name = ''
    self.acronym = ''
    self.v_s = ''
    self.p_s = ''
    self.parent_id = 0
    self.url = ''
    self.old_concept_type = ''
    self.old_nn_id = 0

    # Associations
    self.structures = [] # has_many Structure
    self.neuro_name_structure_synonyms = [] # has_many NeuroNameStructureSynonym

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here