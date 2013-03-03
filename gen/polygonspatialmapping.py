# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class PolygonSpatialMapping(object):
    '''aibs.model.polygonspatialmapping (autogen)'''

    # Fields
    self.id = 0
    self.specimen_id = 0
    self.section_data_set_id = 0
    self.section_image_id = 0
    self.graphic_group_label_id = 0
    self.graphic_object_id = 0
    self.structure_id = 0
    self.section_number = 0
    self.section_image_cx = 0
    self.section_image_cy = 0
    self.cx = 0
    self.cy = 0
    self.mri_cx = 0
    self.mri_cy = 0
    self.mri_cz = 0

    # Associations
    self.specimen = None # belongs_to Specimen
    self.section_data_set = None # belongs_to SectionDataSet
    self.section_image = None # belongs_to SectionImage
    self.graphic_group_label = None # belongs_to GraphicGroupLabel
    self.graphic_object = None # belongs_to GraphicObject
    self.structure = None # belongs_to Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here