import math
def RwySlope(Elev_THS,Elev_far,Length):
    res = (Elev_far - Elev_THS) / Length
    return round(res,2)

