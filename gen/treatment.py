# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Treatment(object):
    '''aibs.model.treatment (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.tags = ''

    # Associations
    self.atlases = [] # has_many Atlas
    self.atlas_infos = [] # has_many AtlasInfo
    self.data_sets = [] # has_and_belongs_to_many DataSet

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here