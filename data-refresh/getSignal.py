import json
import urllib.request
import os

api_server = os.environ.get("API_SERVER", "https://api.when2water.org")

def getSig (zipCode, restriction=-1):
    URL = "{}/?zip={}&restriction={}&json=1".format(api_server, zipCode, restriction)
    #print(URL)
    sig = json.loads(urllib.request.urlopen(URL).read().decode())
    #print(sig)
    return sig['signal']

if __name__ == "__main__":
    print(getSig("01886", 0))
    print(getSig("99801", 1))
    print(getSig("84101", 1))
    print(getSig("10007", 0))
