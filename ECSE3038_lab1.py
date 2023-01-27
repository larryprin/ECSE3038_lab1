import math
def temperaturecheck(temp, g):
    if (((temp < 35) and (g == "C")) or ((temp < 95 ) and (g == "F"))) :
        print("the patient is hypothermic")

    elif (((temp > 40) and (g == "C")) or ((temp > 104 ) and (g == "F"))) :
        print ("the patient is hyperthermic")

    elif (((temp > 35 and temp < 40) and (g == "C")) or ((temp > 95 and temp < 104 ) and (g == "F"))) :
        print("the patient has normal body temperature")
    
    else:
        print("Invalid")


temperaturecheck(56,"F")


def voltdrop(volt,  resist):
    u = sum(resist)
    current = volt/u   
    for x in resist:
        drop = x * current
        print(drop)
     

voltdrop(10,[56,78,90,100])

def parallel(resistors):
    result = 0
    for y in resistors:
        res = (1/y)       
        result = result + res
    damn = 1/result
    print(damn)

   
parallel([600,450,800,1000])
    