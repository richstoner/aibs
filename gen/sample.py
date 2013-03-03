# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Sample(object):
    '''aibs.model.sample (autogen)'''

    # Fields
    self.id = 0
    self.microarray_data_set_id = 0
    self.structure_id = 0
    self.rna_integrity_number = 0.0

    # Associations
    self.microarray_data_set = None # belongs_to MicroarrayDataSet
    self.structure = None # belongs_to Structure
    self.microarray_slides = [] # has_many MicroarraySlide

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here