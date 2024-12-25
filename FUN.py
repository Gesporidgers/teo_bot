import math
import rsa
def RwySlope(Elev_THS,Elev_far,Length):
    res = (Elev_far - Elev_THS) / Length
    return round(res,2)

def FlightLink(Orig, Dest):
    return "https://dispatch.simbrief.com/options/custom?orig="+ Orig.upper() +"&dest="+Dest.upper()

def Encryption(message):
    (pub, priv) = rsa.newkeys(256)
    msg_utf8 = message.encode('utf-8')
    return rsa.encrypt(msg_utf8,pub).hex()