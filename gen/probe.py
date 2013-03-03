# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Probe(object):
    '''aibs.model.probe (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.label = ''
    self.orientation_id = 0
    self.gene_id = 0
    self.predicted_sequence_id = 0
    self.forward_sequence_id = 0
    self.reverse_sequence_id = 0
    self.ncbi_accession_number = ''
    self.gi = 0
    self.probe_type = ''
    self.fluor_color = ''
    self.gc_percent = 0.0
    self.sphinx_id = 0

    # Associations
    self.gene = None # belongs_to Gene
    self.gene_association = None # has_one GeneAssociation
    self.orientation = None # belongs_to Orientation
    self.predicted_sequence = None # belongs_to Sequence
    self.forward_primer_sequence = None # belongs_to Sequence
    self.reverse_primer_sequence = None # belongs_to Sequence
    self.microarray_designs = [] # has_and_belongs_to_many MicroarrayDesign
    self.data_sets = [] # has_and_belongs_to_many DataSet
    self.products = [] # has_and_belongs_to_many Product

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here