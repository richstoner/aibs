# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Transcript(object):
    '''aibs.model.transcript (autogen)'''

    # Fields
    self.id = 0
    self.gene_id = 0
    self.molbio_authority_id = 0
    self.ncbi_accession_number = ''
    self.agilent_upload = None

    # Associations
    self.gene = None # belongs_to Gene
    self.molbio_authority = None # belongs_to MolbioAuthority

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here