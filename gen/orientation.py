# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Orientation(object):
    '''aibs.model.orientation (autogen)'''

    # Fields
    self.id = 0
    self.name = ''

    # Associations
    self.probes = [] # has_many Probe

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here