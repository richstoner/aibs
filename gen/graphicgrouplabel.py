# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class GraphicGroupLabel(object):
    '''aibs.model.graphicgrouplabel (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.color = ''

    # Associations
    self.groups = [] # has_many Group
    self.atlases = [] # has_many Atlas
    self.atlas_infos = [] # has_many AtlasInfo
    self.polygon_spatial_mappings = [] # has_many PolygonSpatialMapping

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here