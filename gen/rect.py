# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Rect(object):
    '''aibs.model.rect (autogen)'''

    # Fields
    self.id = 0
    self.type = ''
    self.order = 0
    self.parent_id = 0
    self.address = ''
    self.graphic_group_label_id = 0
    self.sub_image_id = 0
    self.structure_id = 0
    self.path = ''
    self.mag = 0.0
    self.display_attributes = ''

    # Associations
    self.graphic_transformations = [] # has_many GraphicTransformation
    self.graphic_objects = [] # has_many GraphicObject
    self.clones = [] # has_many GraphicObject
    self.parent = None # belongs_to GraphicObject
    self.template = None # belongs_to GraphicObject
    self.sub_image = None # belongs_to SubImage
    self.polygon_spatial_mappings = [] # has_many PolygonSpatialMapping
    self.group = None # belongs_to Group
    self.section_image = None # belongs_to SectionImage
    self.structure = None # belongs_to Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here