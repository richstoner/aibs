# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Neurosurgery(object):
    '''aibs.model.neurosurgery (autogen)'''

    # Fields
    self.id = 0
    self.donor_id = 0
    self.neurosurgery_reason = ''
    self.neurosurgery_location = ''
    self.neurosurgery_at = None
    self.tissue_type = ''
    self.stereotactic_coordinate_x = 0
    self.stereotactic_coordinate_y = 0
    self.stereotactic_coordinate_z = 0
    self.long_term_hypoxia = ''
    self.primary_tissue_source = ''
    self.secondary_tissue_source = ''
    self.age_id = 0

    # Associations
    self.donor = None # belongs_to Donor
    self.age = None # belongs_to Age

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here