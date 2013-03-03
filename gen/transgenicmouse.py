# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class TransgenicMouse(object):
    '''aibs.model.transgenicmouse (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.transgenic_induction_method_name = ''
    self.transgenic_induction_method_description = ''

    # Associations
    self.donors = [] # has_many Donor
    self.transgenic_lines = [] # has_and_belongs_to_many TransgenicLine

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here