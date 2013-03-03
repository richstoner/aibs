# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class WellKnownFile(object):
    '''aibs.model.wellknownfile (autogen)'''

    # Fields
    self.id = 0
    self.path = ''
    self.attachable_id = 0
    self.attachable_type = ''
    self.well_known_file_type_id = 0
    self.download_link = ''

    # Associations
    self.well_known_file_type = None # belongs_to WellKnownFileType

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here