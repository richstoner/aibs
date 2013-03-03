# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class MicroarrayDesign(object):
    '''aibs.model.microarraydesign (autogen)'''

    # Fields
    self.id = 0
    self.name = ''

    # Associations
    self.microarray_slides = [] # has_many MicroarraySlide
    self.probes = [] # has_and_belongs_to_many Probe

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here