# Code is written and maintained by Arnav Mukhopadhyay
# * Do not misuse. Help this code to save live *
# * Get everyone vaccinated so that we can be have a COVID free World *
# * This code uses CoWin Open API and works when vaccinating in India *
# * Stay Safe and Get Vaccinated *

from api.useragent import getUA
import urllib3
import json

def getStateList():
    header = getUA()
    header["accept"] = "application/json"
    header["Accept-Language"] = "hi_IN"

    url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"

    http = urllib3.PoolManager()
    r = http.request("GET", url, headers=header)
    if r.status != 200:
        return None

    data = json.loads( r.data.decode("UTF-8"))
    states = data["states"]

    state_dict = {}
    for state in states:
        state_dict[state["state_id"]]  = state["state_name"]
    return state_dict


def getDistrictList(state_id):
    header = getUA()
    header["accept"] = "application/json"
    header["Accept-Language"] = "hi_IN"

    url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_id)

    http = urllib3.PoolManager()
    r = http.request("GET", url, headers=header)
    if r.status != 200:
        return None

    data = json.loads(r.data.decode("UTF-8"))["districts"]
    districts = {}
    for dist in data:
        districts[dist["district_id"]] = dist["district_name"]

    return districts

def getDistrictandState():
    dists = {}
    states = getStateList()
    for id, name in states.items():
        districts = getDistrictList(id)
        for d_id, d_name in districts.items():
            fullname = "{},{}".format(d_name, name)
            dists[d_id] = fullname

    return dists


def findDistrictOrState(search):
    search = search.lower().strip()
    all = getDistrictandState()

    found = {}
    for id, name in all.items():
        small = name.lower().strip()
        if search in small:
            found[id] = name

    return found

