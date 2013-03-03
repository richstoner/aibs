# -*- coding: utf-8 -*-
# aibs.model.sectionimage
# Rich Stoner, 2013

class SectionImage(object):
    """docstring for SectionImage"""

    def __init__(self, _tag):
        self.tag =  _tag
        self.metadata = {}
        self.section_number = -1

        # not really sure how to break these up yet
        self.TILE_baseURL = '''http://human.brain-map.org/tiles//'''
        self.TILE_thumbnail = '''/TileGroup/0-0-0.jpg'''
        self.API_imageServiceBase = '''http://api.brain-map.org/cgi-bin/imageservice?path='''

    def __str__(self):
        return '%s - [ %s x %s ]' % (self.tag, self.metadata['width'], self.metadata['height'])

    def __repr__(self):
        return '%s - [ %s x %s ]' % (self.tag, self.metadata['width'], self.metadata['height'])
        

    def generateThumbnailURL(self):
        returnStr = self.TILE_baseURL + self.metadata['path'] + self.TILE_thumbnail
        returnStr += '?siTop=' + self.metadata['y']
        returnStr += '&siLeft=' + self.metadata['x']
        returnStr += '&siWidth=' + self.metadata['width']
        returnStr += '&siHeight=' + self.metadata['height']
        return returnStr

    
    def generateDownSampleURL(self, downsample):
        import math
        returnStr = self.API_imageServiceBase + self.metadata['path']
        returnStr += '&top=' + str(int(self.metadata['y'] / math.pow(2,downsample))) 
        returnStr += '&left=' + str(int(self.metadata['x'] / math.pow(2,downsample))) 
        returnStr += '&width=' + str(int(self.metadata['width'] / math.pow(2,downsample))) 
        returnStr += '&height=' + str(int(self.metadata['height'] / math.pow(2,downsample))) 
        returnStr += '&downsample=' + str(downsample)
        return returnStr









