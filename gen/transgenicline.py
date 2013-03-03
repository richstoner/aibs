# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class TransgenicLine(object):
    '''aibs.model.transgenicline (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.stock_number = ''
    self.transgenic_line_type_name = ''
    self.transgenic_line_type_code = ''
    self.transgenic_line_source_name = ''
    self.originating_lab = ''
    self.url_prefix = ''
    self.url_suffix = ''
    self.description = ''
    self.sub_image_annotation_id = 0

    # Associations
    self.sub_image_annotation = None # belongs_to SubImageAnnotation
    self.transgenic_mice = [] # has_and_belongs_to_many TransgenicMouse
    self.genes = [] # has_and_belongs_to_many Gene

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here