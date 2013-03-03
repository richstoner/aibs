# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Specimen(object):
    '''aibs.model.specimen (autogen)'''

    # Fields
    self.id = 0
    self.donor_id = 0
    self.name = ''
    self.tissue_ph = 0.0
    self.rna_integrity_number = 0.0
    self.hemisphere = ''
    self.structure_id = 0
    self.parent_id = 0
    self.parent_x_coord = 0
    self.parent_y_coord = 0
    self.parent_z_coord = 0
    self.external_specimen_name = ''
    self.specimen_id_path = ''
    self.chemotherapy = ''
    self.egfr_amplification = ''
    self.extent_of_resection = ''
    self.mgmt_pcr = ''
    self.pten_deletion = ''
    self.radiation_therapy = ''
    self.tumor_status = ''
    self.smoker = ''

    # Associations
    self.parent = None # belongs_to Specimen
    self.children = [] # has_many Specimen
    self.ancestor_hierarchies = [] # has_many SpecimenHierarchy
    self.self_and_ancestors = [] # has_many Specimen
    self.descendant_hierarchies = [] # has_many SpecimenHierarchy
    self.self_and_descendants = [] # has_many Specimen
    self.data_sets = [] # has_many DataSet
    self.specimen_images = [] # has_many SpecimenImage
    self.well_known_files = [] # has_many WellKnownFile
    self.injections = [] # has_many Injection
    self.specimen_types = [] # has_and_belongs_to_many SpecimenType
    self.donor = None # belongs_to Donor
    self.structure = None # belongs_to Structure
    self.specimen_condition_values = [] # has_many SpecimenConditionValue
    self.conditions = [] # has_many Condition
    self.alignment3d = None # has_one Alignment3d
    self.atlases = [] # has_many Atlas
    self.atlas_infos = [] # has_many AtlasInfo
    self.polygon_spatial_mappings = [] # has_many PolygonSpatialMapping
    self.annotation_structures = [] # has_and_belongs_to_many Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here