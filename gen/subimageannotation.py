# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class SubImageAnnotation(object):
    '''aibs.model.subimageannotation (autogen)'''

    # Fields
    self.id = 0
    self.sub_image_id = 0
    self.description = ''
    self.width = 0
    self.height = 0
    self.x = 0
    self.y = 0
    self.zoom = 0
    self.abs_x = 0
    self.abs_y = 0
    self.weight = 0
    self.failed = None
    self.sphinx_id = 0

    # Associations
    self.transgenic_line = None # has_one TransgenicLine
    self.sub_image = None # belongs_to SubImage
    self.sub_image_annotation_tags = [] # has_and_belongs_to_many SubImageAnnotationTag

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here