# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class StructureBoundingBox(object):
    '''aibs.model.structureboundingbox (autogen)'''

    # Fields
    self.id = 0
    self.atlas_id = 0
    self.structure_id = 0
    self.section_data_set_id = 0
    self.section_image_id = 0
    self.section_number = 0
    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0

    # Associations
    self.atlas = None # belongs_to Atlas
    self.structure = None # belongs_to Structure
    self.section_data_set = None # belongs_to SectionDataSet
    self.section_image = None # belongs_to SectionImage

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here