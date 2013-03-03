# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Structure(object):
    '''aibs.model.structure (autogen)'''

    # Fields
    self.id = 0
    self.atlas_id = 0
    self.name = ''
    self.acronym = ''
    self.st_level = 0
    self.ontology_id = 0
    self.hemisphere_id = 0
    self.weight = 0
    self.parent_structure_id = 0
    self.depth = 0
    self.graph_id = 0
    self.graph_order = 0
    self.structure_id_path = ''
    self.color_hex_triplet = ''
    self.neuro_name_structure_id = 0
    self.neuro_name_structure_id_path = ''
    self.failed = None
    self.sphinx_id = 0

    # Associations
    self.parent = None # belongs_to Structure
    self.children = [] # has_many Structure
    self.ancestor_hierarchies = [] # has_many StructureHierarchy
    self.self_and_ancestors = [] # has_many Structure
    self.descendant_hierarchies = [] # has_many StructureHierarchy
    self.self_and_descendants = [] # has_many Structure
    self.structure_graph = None # belongs_to StructureGraph
    self.ontology = None # belongs_to Ontology
    self.hemisphere = None # belongs_to Hemisphere
    self.neuro_name_structure = None # belongs_to NeuroNameStructure
    self.specimens = [] # has_many Specimen
    self.structure_sets_structures = [] # has_many StructureSetsStructure
    self.structure_sets = [] # has_many StructureSet
    self.structure_centers = [] # has_many StructureCenter
    self.parent_structure = None # has_one Structure
    self.child_structures = [] # has_many Structure
    self.graph = None # has_one StructureGraph
    self.annotation_infos = [] # has_many AnnotationInfo
    self.atlas_contours = [] # has_many AtlasContour
    self.data_points = [] # has_many DataPoint
    self.fine_structure_searches = [] # has_many FineStructureSearch
    self.injections = [] # has_many Injection
    self.manual_annotations = [] # has_many ManualAnnotation
    self.ontology_nodes = [] # has_many OntologyNode
    self.polygon_spatial_mappings = [] # has_many PolygonSpatialMapping
    self.samples = [] # has_many Sample
    self.shapes = [] # has_many Shape
    self.structure_unionizes = [] # has_many StructureUnionize
    self.sub_images = [] # has_many SubImage

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here