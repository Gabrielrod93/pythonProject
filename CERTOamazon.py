def getMinimumDays(parcels):
    dias = 0
    while max(parcels) != 0:
        while 0 in parcels:
            parcels.remove(0)
        menor = min(parcels)
        for i, v in enumerate(parcels):
            parcels[i] = v - menor
        dias = dias + 1
    return dias



print(getMinimumDays([2,5,0,3,0,5]))