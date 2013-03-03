# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Document(object):
    '''aibs.model.document (autogen)'''

    # Fields
    self.id = 0
    self.heading = ''
    self.title = ''
    self.description = ''
    self.url = ''
    self.tags = ''
    self.product_id = 0
    self.weight = 0
    self.failed = None

    # Associations
    self.product = None # belongs_to Product

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here