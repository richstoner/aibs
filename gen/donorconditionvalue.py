# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class DonorConditionValue(object):
    '''aibs.model.donorconditionvalue (autogen)'''

    # Fields
    self.id = 0
    self.condition_id = 0
    self.donor_id = 0
    self.value = 0.0

    # Associations
    self.donor = None # belongs_to Donor
    self.condition = None # belongs_to Condition

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here