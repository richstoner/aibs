# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class AnnotationInfo(object):
    '''aibs.model.annotationinfo (autogen)'''

    # Fields
    self.id = 0
    self.atlas_id = 0
    self.section_data_set_id = 0
    self.section_image_id = 0
    self.structure_id = 0
    self.specimen_tissue_index = 0
    self.x = 0
    self.y = 0
    self.w = 0
    self.h = 0
    self.max_zoom = 0
    self.filepath = ''
    self.order = 0
    self.path = ''

    # Associations
    self.atlas = None # belongs_to Atlas
    self.section_data_set = None # belongs_to SectionDataSet
    self.section_image = None # belongs_to SectionImage
    self.structure = None # belongs_to Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here