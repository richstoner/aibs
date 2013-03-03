# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class Scale(object):
    '''aibs.model.scale (autogen)'''

    # Fields
    self.id = 0
    self.type = ''
    self.order = 0
    self.sx = 0.0
    self.rx = 0.0
    self.ry = 0.0
    self.sy = 0.0
    self.tx = 0.0
    self.ty = 0.0
    self.a = 0.0
    self.graphic_object_id = 0

    # Associations
    self.graphic_object = None # belongs_to GraphicObject

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here