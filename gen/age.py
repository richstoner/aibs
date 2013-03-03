# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Age(object):
    '''aibs.model.age (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.description = ''
    self.days = 0.0
    self.embryonic = None
    self.organism_id = 0
    self.tags = ''
    self.developmental_stage_id = 0
    self.age_group_id = 0

    # Associations
    self.neurosurgeries = [] # has_many Neurosurgery
    self.organism = None # belongs_to Organism
    self.developmental_stage = None # belongs_to DevelopmentalStage
    self.age_group = None # belongs_to AgeGroup
    self.atlas_infos = [] # has_many AtlasInfo
    self.donors = [] # has_many Donor
    self.injections = [] # has_many Injection
    self.reference_spaces = [] # has_many ReferenceSpace

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here