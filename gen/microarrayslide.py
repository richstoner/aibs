# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class MicroarraySlide(object):
    '''aibs.model.microarrayslide (autogen)'''

    # Fields
    self.id = 0
    self.barcode = ''
    self.microarray_design_id = 0
    self.sample_id = 0
    self.rna_in_array = 0.0
    self.rna_in_labeling_reaction = 0.0

    # Associations
    self.microarray_design = None # belongs_to MicroarrayDesign
    self.microarray_data_sets = [] # has_many MicroarrayDataSet
    self.structures = [] # has_many Structure
    self.sample = None # belongs_to Sample
    self.well_known_files = [] # has_many WellKnownFile

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here