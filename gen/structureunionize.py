# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class StructureUnionize(object):
    '''aibs.model.structureunionize (autogen)'''

    # Fields
    self.id = 0
    self.section_data_set_id = 0
    self.structure_id = 0
    self.sum_pixels = 0.0
    self.sum_expressing_pixels = 0.0
    self.sum_pixel_intensity = 0.0
    self.sum_expressing_pixel_intensity = 0.0
    self.expression_density = 0.0
    self.expression_energy = 0.0
    self.voxel_energy_mean = 0.0
    self.voxel_energy_cv = 0.0

    # Associations
    self.section_data_set = None # belongs_to SectionDataSet
    self.structure = None # belongs_to Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here