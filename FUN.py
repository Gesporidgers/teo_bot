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

def Kendall(message: str):
    smo = message.split('/')
    Result = ""
    SMO_dict = {
        "M" : "Экспоненциальному закону",
        "G" : "Произвольному закону общего вида",
        "U" : "Равномерному закону",
        "D" : "Детерминированному закону"
    }
    not_constant = {
        "E" : "Закону Эрланга",
        "h" : "Гипоэкспоненциальному закону",
        "H" : "Гиперэкспоненциальному закону"
    }
    if smo[0] in SMO_dict:
        Result += f"Входной поток распределён по *{SMO_dict[smo[0]]}*\n\n"
    else:
        Result += f"Входной поток распределён по *{not_constant[smo[0][0]]} {smo[0][1]} порядка*\n\n"
    if smo[1] in SMO_dict:
        Result += f"Выходной поток распределён по *{SMO_dict[smo[1]]}*\n\n"
    else:
        Result += f"Выходной поток распределён по *{not_constant[smo[1][0]]} {smo[1][1]} порядка*\n\n"
    Result += f"СМО имеет _{smo[2]}_ каналов\n\n"
    if len(smo) == 3:
        Result += "У СМО неограниченная очередь"
    else:
        Result += f"СМО имеет {smo[3]} мест в очереди"
    return Result
