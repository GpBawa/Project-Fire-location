import requests
from time import time
import os
from datetime import datetime
import Setup


urls = [
    #(os.path.join(Setup.input_folder, 'NPP.csv'),
     #"https://firms.modaps.eosdis.nasa.gov/data/active_fire/suomi-npp-viirs-c2/csv/SUOMI_VIIRS_C2_South_Asia_24h.csv"),
    (os.path.join(Setup.input_folder, 'NOAA.csv'),
     "https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/csv/J1_VIIRS_C2_South_Asia_24h.csv")
    #(os.path.join(Setup.input_folder, 'Modis.csv'), "https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_South_Asia_24h.csv")
]

def url_response(url):
    path, url = url
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        f.write(r.content)
        print path + ' file downloaded'
    f.close()

def fire_location():
    start = time()
    print('Downloading new fire location...')
    for x in urls:
        url_response(x)
    print('Download Complete...')
    print("Time to download:" + str(time() - start))
