# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class PlaneOfSection(object):
    '''aibs.model.planeofsection (autogen)'''

    # Fields
    self.id = 0
    self.name = ''

    # Associations
    self.atlas_infos = [] # has_many AtlasInfo
    self.data_sets = [] # has_many DataSet

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here