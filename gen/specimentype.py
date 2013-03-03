# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class SpecimenType(object):
    '''aibs.model.specimentype (autogen)'''

    # Fields
    self.id = 0
    self.name = ''

    # Associations
    self.specimens = [] # has_and_belongs_to_many Specimen

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here