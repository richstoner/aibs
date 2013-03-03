# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class ManualAnnotation(object):
    '''aibs.model.manualannotation (autogen)'''

    # Fields
    self.id = 0
    self.structure_id = 0
    self.section_data_set_id = 0
    self.annotation_plan_name = ''
    self.intensity_call = ''
    self.density_call = ''
    self.pattern_call = ''
    self.mixed_population_call = ''
    self.comment = ''

    # Associations
    self.structure = None # belongs_to Structure
    self.section_data_set = None # belongs_to SectionDataSet

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here