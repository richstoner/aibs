# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class AtlasInfo(object):
    '''aibs.model.atlasinfo (autogen)'''

    # Fields
    self.id = 0
    self.organism_name = ''
    self.plane_of_section_name = ''
    self.age_name = ''
    self.atlas_id = 0
    self.structure_graph_id = 0
    self.specimen_id = 0
    self.plane_of_section_id = 0
    self.age_id = 0
    self.atlas_title = ''
    self.xyz_sort = ''
    self.treatment_id = 0
    self.graphic_group_label_id = 0

    # Associations
    self.atlas = None # belongs_to Atlas
    self.structure_graph = None # belongs_to StructureGraph
    self.specimen = None # belongs_to Specimen
    self.plane_of_section = None # belongs_to PlaneOfSection
    self.age = None # belongs_to Age
    self.treatment = None # belongs_to Treatment
    self.graphic_group_label = None # belongs_to GraphicGroupLabel

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here