# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class RikenGene(object):
    '''aibs.model.rikengene (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.entrez_id = 0
    self.acronym = ''
    self.organism_id = 0
    self.chromosome_id = 0
    self.homologene_id = 0
    self.type = ''
    self.legacy_ensembl_gene_id = 0
    self.ensembl_id = ''
    self.alias_tags = ''
    self.sphinx_id = 0

    # Associations
    self.organism = None # belongs_to Organism
    self.transcripts = [] # has_many Transcript
    self.gene_tags = [] # has_and_belongs_to_many GeneTag
    self.gene_classifications = [] # has_and_belongs_to_many GeneClassification
    self.chromosome = None # belongs_to Chromosome
    self.gene_aliases = [] # has_many GeneAlias
    self.probes = [] # has_many Probe
    self.gene_lookups = [] # has_many GeneLookup
    self.gene_classification_counts = [] # has_many GeneClassificationCount
    self.products = [] # has_and_belongs_to_many Product
    self.data_sets = [] # has_many DataSet
    self.gene_associations = [] # has_many GeneAssociation
    self.transgenic_lines = [] # has_and_belongs_to_many TransgenicLine
    self.molbio_authority = None # belongs_to MolbioAuthority
    self.data_points = [] # has_many DataPoint
    self.homologous_gene_associations = [] # has_many HomologousGeneAssociation
    self.homologous_genes = [] # has_many Gene
    self.ensembl_genes = [] # has_and_belongs_to_many EnsemblGene
    self.ncbi_genes = [] # has_and_belongs_to_many NcbiGene
    self.rnaseq_designs = [] # has_and_belongs_to_many RnaseqDesign

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here