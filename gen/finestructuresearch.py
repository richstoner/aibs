# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class FineStructureSearch(object):
    '''aibs.model.finestructuresearch (autogen)'''

    # Fields
    self.id = 0
    self.section_data_set_id = 0
    self.structure_id = 0
    self.gene_rank = 0.0

    # Associations
    self.structure = None # belongs_to Structure
    self.section_data_set = None # belongs_to SectionDataSet

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here