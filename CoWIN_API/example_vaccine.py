# Code is written and maintained by Arnav Mukhopadhyay
# * Do not misuse. Help this code to save live *
# * Get everyone vaccinated so that we can be have a COVID free World *
# * This code uses CoWin Open API and works when vaccinating in India *
# * Stay Safe and Get Vaccinated *



from api.vaccine import getVaccineByDistrict, getVaccineByDistrictByDate, getVaccineByDistrictByDateRange

from datetime import datetime

now= datetime.now()
#l = getVaccineByDistrict(district=725, day=now.day, month=now.month, year=now.year, dose=2)
#print(l)

#l1 = getVaccineByDistrictByDate(district=725, day=now.day, month=now.month, year=now.year, dose=2)
#print(l1)

l2 = getVaccineByDistrictByDateRange(district=725, day=now.day, month=now.month, year=now.year, dose=2, spanDays=60, minAge=0, maxAge=100)
print(l2)
print(len(l2))