# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Injection(object):
    '''aibs.model.injection (autogen)'''

    # Fields
    self.id = 0
    self.specimen_id = 0
    self.injection_quality = ''
    self.days_post_injection = 0
    self.targeted_injection_structure_id = 0
    self.injection_method = ''
    self.angle = 0
    self.coordinates_ap = ''
    self.coordinates_ml = ''
    self.coordinates_dv = ''
    self.primary_injection_structure_id = 0
    self.injection_materials = ''
    self.fluor_colors = ''
    self.structure_id = 0
    self.age_id = 0

    # Associations
    self.specimen = None # belongs_to Specimen
    self.structure = None # belongs_to Structure
    self.age = None # belongs_to Age
    self.primary_injection_structure = None # belongs_to Structure
    self.targeted_injection_structure = None # belongs_to Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here