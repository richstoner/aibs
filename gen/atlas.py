# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Atlas(object):
    '''aibs.model.atlas (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.structure_graph_id = 0
    self.specimen_id = 0
    self.xyz_sort = ''
    self.treatment_id = 0
    self.graphic_group_label_id = 0
    self.reference_space_id = 0

    # Associations
    self.structure_graph = None # belongs_to StructureGraph
    self.specimen = None # belongs_to Specimen
    self.treatment = None # belongs_to Treatment
    self.graphic_group_label = None # belongs_to GraphicGroupLabel
    self.reference_space = None # belongs_to ReferenceSpace
    self.atlas_data_sets = [] # has_and_belongs_to_many AtlasDataSet
    self.annotation_infos = [] # has_many AnnotationInfo
    self.atlas_contours = [] # has_many AtlasContour
    self.atlas_infos = [] # has_many AtlasInfo

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here