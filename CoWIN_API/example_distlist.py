from api.statelist import getDistrictandState

all = getDistrictandState()
for id, name in all.items():
    print(id,"=", name)