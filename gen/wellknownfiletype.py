# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class WellKnownFileType(object):
    '''aibs.model.wellknownfiletype (autogen)'''

    # Fields
    self.id = 0
    self.name = ''

    # Associations
    self.well_known_files = [] # has_many WellKnownFile

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here