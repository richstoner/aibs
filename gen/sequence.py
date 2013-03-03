# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Sequence(object):
    '''aibs.model.sequence (autogen)'''

    # Fields
    self.id = 0
    self.sequence_data = ''
    self.sequence_length = 0

    # Associations
    self.probes = [] # has_many Probe

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here