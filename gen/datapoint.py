# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class DataPoint(object):
    '''aibs.model.datapoint (autogen)'''

    # Fields
    self.id = 0
    self.gene_id = 0
    self.product_id = 0
    self.structure_id = 0
    self.data_point_type_id = 0
    self.weight = 0
    self.failed = None
    self.treatment_id = 0

    # Associations
    self.gene = None # belongs_to Gene
    self.product = None # belongs_to Product
    self.structure = None # belongs_to Structure
    self.treatment = None # belongs_to Treatment
    self.data_point_type = None # belongs_to DataPointType
    self.donors = [] # has_and_belongs_to_many Donor

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here