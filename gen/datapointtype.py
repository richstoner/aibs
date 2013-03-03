# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class DataPointType(object):
    '''aibs.model.datapointtype (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.tags = ''
    self.description = ''

    # Associations
    self.data_points = [] # has_many DataPoint

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here