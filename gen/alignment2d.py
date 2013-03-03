# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Alignment2d(object):
    '''aibs.model.alignment2d (autogen)'''

    # Fields
    self.id = 0
    self.tvs_00 = 0.0
    self.tvs_01 = 0.0
    self.tvs_02 = 0.0
    self.tvs_03 = 0.0
    self.tvs_04 = 0.0
    self.tvs_05 = 0.0
    self.tsv_00 = 0.0
    self.tsv_01 = 0.0
    self.tsv_02 = 0.0
    self.tsv_03 = 0.0
    self.tsv_04 = 0.0
    self.tsv_05 = 0.0
    self.section_image_id = 0

    # Associations
    self.section_image = None # belongs_to SectionImage

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here