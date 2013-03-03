# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class AffymetrixMacaqueProbeset(object):
    '''aibs.model.affymetrixmacaqueprobeset (autogen)'''

    # Fields
    self.id = 0
    self.displayable_id_from_affymetrix = ''

    # Associations
    self.gene_association = None # has_one GeneAssociation

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here