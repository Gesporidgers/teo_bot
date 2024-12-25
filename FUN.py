import math
def RwySlope(Elev_THS,Elev_far,Length):
    res = (Elev_far - Elev_THS) / Length
    return round(res,2)

def FlightLink(Orig, Dest):
    return "https://dispatch.simbrief.com/options/custom?orig="+ Orig +"&dest="+Dest

def Encryption():
    pass