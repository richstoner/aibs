# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Condition(object):
    '''aibs.model.condition (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.description = ''

    # Associations
    self.donor_condition_values = [] # has_many DonorConditionValue
    self.donors = [] # has_many Donor
    self.specimen_condition_values = [] # has_many SpecimenConditionValue
    self.specimens = [] # has_many Specimen

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here