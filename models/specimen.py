
class Specimen(object):
    ''' the generic AIBS specimen object'''

    def __init__(self, remote=True, subjectName='undefined'):

        self.subjectName = subjectName
        self.remoteSpecimen = True
        self.metadata = {}
        self.sectionImageList = []

        self.markersOfInterest = []
        self.allMarkers = []
        self.filteredMarkers = []

       # print 'Initialized a new specimen: %s (remote: %s)' % (self.subjectName, str(self.remoteSpecimen))


    def getListOfAvailableMarkers(self):

        if self.remoteSpecimen:

            import requests
            API_baseDetailString = '''http://human.brain-map.org/api/v2/data/Specimen/%d.json?wrap=true&include=donor(age,conditions),data_sets(products[id$in9,10,11,26,27],genes,treatments),specimen_images,specimen_types,well_known_files,structure'''
            specimenDetailJSON = API_baseDetailString % self.metadata['id']
            d = requests.get(specimenDetailJSON)

            if d.status_code == 200:
                if type(d.json) == type(dict()):
                    if d.json['num_rows'] > 0:
                        return d.json['msg'][0]['data_sets']
                else:
                    if d.json()['num_rows'] > 0:
                        return d.json()['msg'][0]['data_sets']
            else:
                return []

        else:
            print 'not implemented yet'


    def getMarkerList(self, verbose=True):
        ''' returns marker list, filtered if wanted'''

        details = self.getListOfAvailableMarkers()
        if type(details) == type(None):
            if verbose:
                print 'no markers found'
            return

        specimenMarkerSet = []
        specimenFilteredMarkerSet = []

        for ds in details:
            
            geneSingle = {}
            
            if ds['treatments'][0]['tags'] == 'histology':
                if verbose:
                    print '%d - HIS: %s' % (ds['id'], ds['treatments'][0]['name'])
                
                geneSingle['id'] = ds['id']
                geneSingle['type'] = 'HIS'
                geneSingle['name'] = ds['treatments'][0]['name']
                
            elif ds['treatments'][0]['tags'] == 'In Situ Hybridization histology':
                
                for gene in ds['genes']:
                    if verbose:
                        print '%d - ISH: %s - %s' % (ds['id'], gene['acronym'], gene['name']) 
                    
                    geneSingle['id'] = ds['id']
                    geneSingle['type'] = 'ISH'
                    geneSingle['name'] = gene['acronym']
            
            specimenMarkerSet.append(geneSingle)

            if geneSingle['name'] in self.markersOfInterest:
                specimenFilteredMarkerSet.append(geneSingle)

            self.filteredMarkers = specimenFilteredMarkerSet
            self.allMarkers = specimenMarkerSet
            
            
            # what do i need to do next???


    def getSectionImages(self, onlyFiltered=True):
        self.sectionImageList = []
        
        list_to_use = []
        if onlyFiltered:
            list_to_use = self.filteredMarkers
        else:
            list_to_use = self.allMarkers

        for sds in list_to_use:
            import aibs
            api = aibs.api()

            imageList = api.getSectionImagesForID(sds['id'])
            self.sectionImageList += imageList

        return self.sectionImageList            


    def getSortedImageList(self):
        import operator
        list_to_sort = self.sectionImageList
        list_to_sort.sort(key=operator.attrgetter('section_number'))
        return list_to_sort


    def printSpecimenDetails(self):

        import pprint
        print('all markers')
        pprint.pprint(self.allMarkers)

        print('filtered markers')
        pprint.pprint(self.filteredMarkers)

        print('section image list')
        pprint.pprint(self.sectionImageList)


        
