# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class DiseaseCategory(object):
    '''aibs.model.diseasecategory (autogen)'''

    # Fields
    self.id = 0
    self.condition_value = ''

    # Associations
    self.donors = [] # has_and_belongs_to_many Donor

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here