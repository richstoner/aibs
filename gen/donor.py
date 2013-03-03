# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Donor(object):
    '''aibs.model.donor (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.age_id = 0
    self.organism_id = 0
    self.strain = ''
    self.sex = ''
    self.transgenic_mouse_id = 0
    self.handedness = ''
    self.pmi = 0.0
    self.condition_description = ''
    self.external_donor_name = ''
    self.sex_full_name = ''
    self.tags = ''
    self.multifocal = ''
    self.recurrence_by_six_months = ''
    self.sleep_state = ''
    self.smoker = ''
    self.theiler_stage = ''

    # Associations
    self.age = None # belongs_to Age
    self.organism = None # belongs_to Organism
    self.transgenic_mouse = None # belongs_to TransgenicMouse
    self.specimens = [] # has_many Specimen
    self.donor_condition_values = [] # has_many DonorConditionValue
    self.conditions = [] # has_many Condition
    self.products = [] # has_and_belongs_to_many Product
    self.data_points = [] # has_and_belongs_to_many DataPoint
    self.disease_categories = [] # has_and_belongs_to_many DiseaseCategory
    self.medical_conditions = [] # has_and_belongs_to_many MedicalCondition
    self.neurosurgeries = [] # has_many Neurosurgery

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here