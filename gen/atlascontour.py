# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class AtlasContour(object):
    '''aibs.model.atlascontour (autogen)'''

    # Fields
    self.id = 0
    self.atlas_id = 0
    self.section_image_id = 0
    self.structure_id = 0
    self.graphic_group_id = 0
    self.contour_id = 0
    self.svg_transformation_matrix = []
    self.svg_transformation_string = ''
    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0
    self.max_zoom = 0
    self.file_path = ''
    self.specimen_order = []
    self.section_number = 0
    self.contour_order = 0
    self.contour_path = ''

    # Associations
    self.atlas = None # belongs_to Atlas
    self.section_image = None # belongs_to SectionImage
    self.structure = None # belongs_to Structure
    self.group = None # belongs_to Group

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here