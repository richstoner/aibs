# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class SpecimenImage(object):
    '''aibs.model.specimenimage (autogen)'''

    # Fields
    self.id = 0
    self.type = ''
    self.path = ''
    self.x = 0
    self.y = 0
    self.width = 0
    self.height = 0
    self.section_number = 0
    self.failed = None
    self.specimen_id = 0
    self.data_set_id = 0
    self.resolution = 0.0
    self.tier_count = 0
    self.expression_path = ''
    self.image_width = 0
    self.image_height = 0
    self.annotated = None
    self.structure_id = 0
    self.image_type = ''
    self.lims1_id = 0

    # Associations
    self.structure = None # belongs_to Structure
    self.data_set = None # belongs_to DataSet
    self.graphic_objects = [] # has_many GraphicObject
    self.alternate_images = [] # has_many AlternateImage
    self.sub_image_annotations = [] # has_many SubImageAnnotation
    self.specimen = None # belongs_to Specimen

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here