# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Equalization(object):
    '''aibs.model.equalization (autogen)'''

    # Fields
    self.id = 0
    self.red_lower = 0
    self.red_upper = 0
    self.green_lower = 0
    self.green_upper = 0
    self.blue_lower = 0
    self.blue_upper = 0
    self.red_mean = 0.0
    self.red_std_dev = 0.0
    self.green_mean = 0.0
    self.green_std_dev = 0.0
    self.blue_mean = 0.0
    self.blue_std_dev = 0.0
    self.section_data_set_id = 0

    # Associations
    self.section_data_set = None # belongs_to SectionDataSet

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here