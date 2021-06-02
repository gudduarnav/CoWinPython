from api.statelist import findDistrictOrState
from api.vaccine import getVaccineByDistrictByDateRange

from datetime import datetime

# setup
search = [
    "karnataka",
    "west bengal"
    ] # district or state

now = datetime.now()
dd = now.day
mm = now.month
yyyy = now.year

span = 30  # days

minAge = 0 # years
maxAge = 100  # years

dose = 2  # 1 = First Dose, 2 = Second Dose


# run the search
for search1 in search:
    l = findDistrictOrState(search1)

    for id, name in l.items():
        print()
        print(id,name)

        lvac = getVaccineByDistrictByDateRange(district=id,
                                               day=dd, month=mm, year=yyyy,
                                               dose=dose,
                                               spanDays=span,
                                               minAge=minAge,
                                               maxAge=maxAge)

        for vac in lvac:
            print("Vaccine Dose:", vac["dose"])
            print("\t",vac["name"], ",", vac["block_name"], ",", vac["district_name"], ",", vac["state_name"], "-", vac["pincode"])
            print("\t","Google Map:", vac["map"])
            print("\t",vac["date"],":", vac["from"], "to", vac["to"])
            print("\t","Slot:", vac["slot"])
            print("\t","Type:", vac["type"])
            print("\t",vac["vaccine"],"will cost Rs.", vac["fees"])
            print("\t",vac["available_capacity"],"are available")
            print()

        print()
    print()