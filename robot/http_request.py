import requests
def serverRequest(distance1, distance2, distance3):
    url = "http://192.168.0.130:8080/sendSensorData?distanceFront="+str(distance1)+"&distanceRight="+str(distance2)+"&distanceLeft="+str(distance3)
    try:
        r = requests.get(url)
    except:
        print('error sending data')