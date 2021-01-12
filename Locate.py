import os
import csv
import datetime
import requests
import Setup

def village():
    locations = []


    print(str(datetime.datetime.today()))
    loc = os.listdir(Setup.output_folder)
    for file in loc:
        if file.endswith(".csv"):
            print("Processing " + str(file))
            infile = os.path.join(Setup.output_folder, file)
            outfile = str(file)+str(datetime.datetime.today()).split()[0]+'.csv'
            csv_writer = open(outfile, 'w')
            csv_writer.write('State,District,Block,Village,longitude,latitude,acq_date,acq_time\n')
            with open(infile, mode='r') as csv_reader:
                record = csv.reader(csv_reader)
                rows = list(record)
                for cell in rows[1:]:
                    latitude = cell[0]
                    longitude = cell[1]
                    print latitude, longitude

                    try:
                        response = requests.get(
                                    'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + latitude + ',' + longitude + '&key=AIzaSyB7DjJvNTqtsMUKR-SCwaGl3V-8VHkaslU')
                    except:
                          continue
                    geo = response.json()
                    district = None
                    state = None
                    village = None
                    block = None
                    data = []
                    try:
                        for x in range(len(geo['results'][0]['address_components'])):
                            if geo['results'][0]['address_components'][x]['types'][0] == "administrative_area_level_1":
                                state = geo['results'][0]['address_components'][x]['long_name']
                            elif geo['results'][0]['address_components'][x]['types'][0] == "administrative_area_level_2":
                                district = geo['results'][0]['address_components'][x]['long_name']
                            elif geo['results'][0]['address_components'][x]['types'][0] == "locality":
                                village = geo['results'][0]['address_components'][x]['long_name']
                    except Exception as e:
                        print(e)
                    data.append(state)
                    data.append(district)
                    data.append(block)
                    data.append(village)
                    data.append(longitude)
                    data.append(latitude)
                    #data.append(cell[5])
                    #data.append(cell[6])
                    locations.append(data)
                    print locations
                    csv_writer.writelines(str(locations))
            csv_writer.close()
            csv_reader.close()
