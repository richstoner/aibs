# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class VirtualMicroarray(object):
    '''aibs.model.virtualmicroarray (autogen)'''

    # Fields
    self.id = 0
    self.probe_id = 0
    self.specimen_id = 0

    # Associations
    self.probe = None # belongs_to Probe
    self.specimen = None # belongs_to Specimen

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here