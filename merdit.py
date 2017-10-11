import requests
from urllib.parse import urlencode, urlparse, parse_qs
import json
import time

class Merdit:
    def __init__(self):
        #base url
        self.base_url = 'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno'    


    def get_stationCode_by_trainNumber (self, train_number):

        url = '/'.join((self.base_url, 'cercaNumeroTrenoTrenoAutocomplete', train_number))
        req = requests.get(url)
        result = None
        if req.status_code == 200:
            content = req.text.rstrip()

            if content:            
                contents = content.split('-')
                if len(contents) != 0:
                    result = contents[2]
        
        return result

    def get_trainState (self, train_number):

        result = None    
        station_code = self.get_stationCode_by_trainNumber(train_number)

        if (station_code is not None):
            url = '/'.join((self.base_url, 'andamentoTreno', station_code, train_number))
            req = requests.get(url)

            if req.status_code == 200:            
                content = req.json()
                result = content["ritardo"]
        
        return result
