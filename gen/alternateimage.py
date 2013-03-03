# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class AlternateImage(object):
    '''aibs.model.alternateimage (autogen)'''

    # Fields
    self.id = 0
    self.sub_image_id = 0
    self.path = ''
    self.image_type = ''

    # Associations
    self.sub_image = None # belongs_to SubImage

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here