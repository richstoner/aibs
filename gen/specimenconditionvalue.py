# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class SpecimenConditionValue(object):
    '''aibs.model.specimenconditionvalue (autogen)'''

    # Fields
    self.id = 0
    self.condition_id = 0
    self.specimen_id = 0
    self.value = 0.0

    # Associations
    self.specimen = None # belongs_to Specimen
    self.condition = None # belongs_to Condition

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here