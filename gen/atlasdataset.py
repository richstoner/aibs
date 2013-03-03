# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class AtlasDataSet(object):
    '''aibs.model.atlasdataset (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.type = ''
    self.specimen_id = 0
    self.plane_of_section_id = 0
    self.failed = None
    self.section_thickness = 0
    self.qc_date = None
    self.expression = None
    self.storage_directory = ''
    self.reference_space_id = 0
    self.weight = 0
    self.sphinx_id = 0
    self.rnaseq_design_id = 0

    # Associations
    self.specimen = None # belongs_to Specimen
    self.plane_of_section = None # belongs_to PlaneOfSection
    self.reference_space = None # belongs_to ReferenceSpace
    self.section_images = [] # has_many SectionImage
    self.sub_images = [] # has_many SubImage
    self.well_known_files = [] # has_many WellKnownFile
    self.treatments = [] # has_and_belongs_to_many Treatment
    self.probes = [] # has_and_belongs_to_many Probe
    self.genes = [] # has_many Gene
    self.products = [] # has_and_belongs_to_many Product
    self.structure_unionizes = [] # has_many StructureUnionize
    self.fine_structure_searches = [] # has_many FineStructureSearch
    self.manual_annotations = [] # has_many ManualAnnotation
    self.alignment3d = None # has_one Alignment3d
    self.equalization = None # has_one Equalization
    self.annotation_infos = [] # has_many AnnotationInfo
    self.polygon_spatial_mappings = [] # has_many PolygonSpatialMapping
    self.atlas_images = [] # has_many AtlasImage
    self.atlases = [] # has_and_belongs_to_many Atlas

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here