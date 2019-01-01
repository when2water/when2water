import urllib.request
from getSignal import getSig
import sys
import traceback
import os

zipFile = os.path.join(os.environ['DATA_LOCATION'], 'zips.txt')
zipList = open(zipFile).readlines()
#print(zipList)

for zips in zipList:
    try:
        if zips == "":
            continue
        #print(zips.strip())
        signal = getSig(zips.strip())
        print("Zip:{zipC}->{signal}".format(zipC=zips.strip(), signal=signal))
 #       0/0
    except:
        traceback.print_exc(file=sys.stderr)
