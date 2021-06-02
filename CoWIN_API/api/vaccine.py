from api.useragent import getUA
import urllib3
import json
from urllib.parse import quote_plus
from datetime import datetime, timedelta

def getVaccineByDistrict(district, day, month, year, minAge = 0, maxAge = 45, dose=1):
    header = getUA()
    header["accept"] = "application/json"
    header["Accept-Language"] = "hi_IN"

    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}-{}-{}".format(
        district, day, month, year
    )

    http = urllib3.PoolManager()
    r = http.request("GET", url, headers=header)
    if r.status != 200:
        return None

    data = json.loads(r.data.decode("UTF-8"))["centers"]
    all_center = list()
    for data1 in data:
        sessions = data1["sessions"]
        for session in sessions:
            if session["min_age_limit"] >= minAge and session["min_age_limit"] < maxAge:
                av = session["available_capacity"]

                if av > 0:
                    for slot in session["slots"]:
                        if "free" in data1["fee_type"].lower():
                            address = {}
                            address["center_id"] = data1["center_id"]
                            address["name"] = data1["name"]
                            address["state_name"] = data1["state_name"]
                            address["district_name"] = data1["district_name"]
                            address["block_name"] = data1["block_name"]
                            address["pincode"] = data1["pincode"]
                            address["lat"] = data1["lat"]
                            address["long"] = data1["long"]
                            address["map"] = "https://www.google.com/maps/place/{}/@{},{}".format(
                                quote_plus(data1["name"]), data1["lat"], data1["long"])
                            address["from"] = data1["from"]
                            address["to"] = data1["to"]
                            address["fee_type"] = data1["fee_type"]
                            address["session_id"] = session["session_id"]
                            address["date"] = session["date"]
                            address["min_age"] = session["min_age_limit"]
                            address["available_capacity"] = int(session["available_capacity_dose{}".format(dose)])
                            address["slot"] = slot
                            address["vaccine"] = session["vaccine"]
                            address["fees"] = 0
                            address["type"] = "free"
                            address["dose"] = dose
                            if address["available_capacity"] > 0:
                                all_center.append(address)
                        else:
                            for vaccine_fees in data1["vaccine_fees"]:
                                address = {}
                                address["center_id"] = data1["center_id"]
                                address["name"] = data1["name"]
                                address["state_name"] = data1["state_name"]
                                address["district_name"] = data1["district_name"]
                                address["block_name"] = data1["block_name"]
                                address["pincode"] = data1["pincode"]
                                address["lat"] = data1["lat"]
                                address["long"] = data1["long"]
                                address["map"] = "https://www.google.com/maps/place/{}/@{},{}".format(
                                    quote_plus(data1["name"]), data1["lat"], data1["long"])
                                address["from"] = data1["from"]
                                address["to"] = data1["to"]
                                address["fee_type"] = data1["fee_type"]
                                address["session_id"] = session["session_id"]
                                address["date"] = session["date"]
                                address["min_age"] = session["min_age_limit"]
                                address["available_capacity"] = int(session["available_capacity_dose{}".format(dose)])
                                address["slot"] = slot
                                address["vaccine"] = vaccine_fees["vaccine"]
                                address["fees"] = vaccine_fees["fee"]
                                address["type"] = "paid"
                                address["dose"] = dose
                                if address["available_capacity"] > 0:
                                    all_center.append(address)

    return all_center


def getVaccineByDistrictByDate(district, day, month, year, minAge = 0, maxAge = 45, dose=1):
    data = getVaccineByDistrict(district, day, month, year, minAge, maxAge, dose)
    if data is None:
        return []

    if len(data) < 1:
        return []

    all = list()
    for data1 in data:
        dd, mm, yyyy = list(map(int, str(data1["date"]).split("-")))
        if dd == day and mm == month and yyyy == year:
            all.append(data1)

    return all


def getVaccineByDistrictByDateRange(district, day, month, year, spanDays=31, minAge = 0, maxAge = 45, dose=1):
    frm = datetime(year, month, day)
    to = frm + timedelta(days=spanDays)

    now = frm
    all = list()
    while now < to:
        oneday = getVaccineByDistrictByDate(district, now.day, now.month, now.year, minAge, maxAge, dose)
        for oneday1 in oneday:
            all.append(oneday1)

        now = now + timedelta(days=1)
    return all
