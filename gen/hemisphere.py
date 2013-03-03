# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Hemisphere(object):
    '''aibs.model.hemisphere (autogen)'''

    # Fields
    self.id = 0
    self.name = ''
    self.symbol = ''

    # Associations
    self.structures = [] # has_many Structure

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here