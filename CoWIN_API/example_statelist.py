from api.statelist import getStateList, getDistrictList

print("State List")
for id, name in getStateList().items():
    print(id, name)
    dist = getDistrictList(id)
    for id1, name1 in dist.items():
        print("\t\t", id1, name1)


