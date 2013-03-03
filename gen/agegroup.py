# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class AgeGroup(object):
    '''aibs.model.agegroup (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.order = 0

    # Associations
    self.ages = [] # has_many Age

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here