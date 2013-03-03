# -*- coding: utf-8 -*-
# Rich Stoner, 2013

class SubImageAnnotationTag(object):
    '''aibs.model.subimageannotationtag (autogen)'''

    # Fields
    self.id = 0
    self.name = ''

    # Associations
    self.sub_image_annotations = [] # has_and_belongs_to_many SubImageAnnotation

    def __init__(self, initialData={}):
        for k,v in initData.iteritems():
            setattr(self, k, v)
        

    # add class methods and private methods here