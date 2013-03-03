# -*- coding: utf-8 -*-
# aibs.api
# Rich Stoner, 2013

import requests

class api(object):

    def __init__(self):
        self.API_listOfSpecimens = '''http://api.brain-map.org/api/v2/data/query.json?criteria=model::Specimen,rma::criteria,donor(products[abbreviation$eqHumanASD]),rma::options[num_rows$eq100]'''
        self.API_baseDetailString = '''http://human.brain-map.org/api/v2/data/Specimen/%d.json?wrap=true&include=donor(age,conditions),data_sets(products[id$in9,10,11,26,27],genes,treatments),specimen_images,specimen_types,well_known_files,structure'''
        self.API_listOfImages = '''http://api.brain-map.org/api/v2/data/SectionDataSet/%d.json?include=section_images'''
        self.TILE_baseURL = '''http://human.brain-map.org/tiles//'''
        self.TILE_thumbnail = '''/TileGroup/0-0-0.jpg'''
        self.API_imageServiceBase = '''http://api.brain-map.org/cgi-bin/imageservice?path='''

    def getSpecimensWithName(self, sname):

        specimen_of_interest = []

        for specimenToCopy in self._getListOfAutism():
            if sname in specimenToCopy['name']:
                s = Specimen(remote=True, subjectName=sname)
                s.metadata = specimenToCopy
                specimen_of_interest.append(s)

        return specimen_of_interest

    def getValidSpecimentsWithName(self, sname):

        speclist = self.getSpecimensWithName(sname);

        explist = []
        for s in speclist:
            s.getMarkerList(verbose=False)
            if len(s.allMarkers) > 0:
                explist.append(s)

        return explist


    def _getListOfAutism(self):
        import requests
        r = requests.get(self.API_listOfSpecimens)
        if r.status_code == 200:
            return self._jsonhelper(r)

    def _jsonhelper(self, resp):
        list_to_return = []
        if type(resp.json) == type(dict()):
            if resp.json['num_rows'] > 0:
                list_to_return = resp.json['msg']
        else:
            if resp.json()['num_rows'] > 0:
                list_to_return = resp.json()['msg']
        return list_to_return
    


    def getImageListForID(self, series_id):
        requestURL = self.API_listOfImages % series_id
        r = requests.get(requestURL)

        seriesImageData = []
        if r.status_code == 200:
            seriesImageData = self._jsonhelper(r)


        if(type(seriesImageData) == type(list())):
            seriesImageData = seriesImageData[0]

        return seriesImageData


    def getSectionImagesForID(self, series_id, sorted=True):

        list_to_return = []

        sds = self.getImageListForID(series_id)
        sectionList = sds['section_images']

        if sorted == True:
            import operator
            sectionList.sort(key=operator.itemgetter('section_number'))


        for si in sectionList:
            tag = '%03d-%s' % (si['section_number'], series_id)

            s = SectionImage(tag)
            s.metadata = si
            s.section_number = si['section_number']

            list_to_return.append(s)

        return list_to_return


    def getDSImagesFromListToPath(self, imageList, _path, ds=5, redownload=False):
        import urllib, os

        for img in imageList:
            dsurl =  img.generateDownSampleURL(ds)
            outputname = '%s/%s-%s-DSx%d.jpg' % (_path, img.tag, img.metadata['id'], ds)
            if not os.path.exists(outputname) or redownload:
                urllib.urlretrieve(dsurl, outputname)
                #print 'downloaded: %s to %s' % (dsurl, outputname)
            else:
                #print 'exists  : %s' % (outputname)
                pass

    

