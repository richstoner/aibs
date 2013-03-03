# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class ReferenceSpace(object):
    '''aibs.model.referencespace (autogen)'''

    # Fields
    self.id = 0
    self.organism_id = 0
    self.age_id = 0
    self.anatomy = ''
    self.name = ''
    self.storage_directory = ''

    # Associations
    self.organism = None # belongs_to Organism
    self.age = None # belongs_to Age
    self.products = [] # has_and_belongs_to_many Product
    self.well_known_files = [] # has_many WellKnownFile
    self.atlases = [] # has_many Atlas
    self.data_sets = [] # has_many DataSet
    self.reference_to_reference_transforms = [] # has_many ReferenceToReferenceTransform
    self.structure_centers = [] # has_many StructureCenter

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here