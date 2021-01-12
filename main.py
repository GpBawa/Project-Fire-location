# This is a sample Python script.
import download
import Locate
import Filter
import Setup

import Farmer

if __name__ == '__main__':
    print 'Statring main process...'
    Setup
    #download.fire_location()
    Filter.filter_data()
    Locate.village()
    Farmer.locate()
    print 'Script completed Successfully...'




