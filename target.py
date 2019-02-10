import sys
import urllib.request, json
'''
route = sys.argv[1]
stop = sys.argv[2]
direction = sys.argv[3]
'''
#Input Arguments
route = input('Route = ')
stop = input('Stop = ')
direction = input('Direction = ')

#print(route, stop, direction)

#URL to find route
url1 = "http://svc.metrotransit.org/NexTrip/Routes?format=json"

res = urllib.request.urlopen(url1)
data =res.read()
file = open("route.json",'wb')
file.write(data)
json_data = json.loads(data)
try:
    for item in json_data:
        if(item['Description'] == route ):
            #print('Route=',item['Description'])
            #print('Route no.=', item['Route'])
            route_num = item['Route']

#URL to find Direction
    url2 = "http://svc.metrotransit.org/NexTrip/Directions/"+route_num+"?format=json"
    res = urllib.request.urlopen(url2)
    data =res.read()
    file = open("direction.json",'wb')
    file.write(data)
    json_data = json.loads(data)
    #print(json_data)
    for item in json_data:
        dirc = item['Text']
        if(direction.lower() in dirc.lower()):
            #print("Direction=",dirc)
            dir_num = item['Value']
except:
    print("Route invalid")
    sys.exit(1)
    
try:
#URL to find Stop
    url3 = "http://svc.metrotransit.org/NexTrip/Stops/"+route_num+"/"+dir_num+"?format=json"
    res = urllib.request.urlopen(url3)
    data =res.read()
    file = open("stop.json",'wb')
    file.write(data)
    json_data = json.loads(data)

    for item in json_data:
        if(item['Text'] == stop):
            #print(item['Text'])
            #print(item['Value'])
            stop_num = item['Value']
    
except:
    print("Direction invalid")
    sys.exit(1)

try:
    try:
#URL to find Next Bus
        url4 = "http://svc.metrotransit.org/NexTrip/"+route_num+"/"+dir_num+"/"+stop_num+"?format=json"
    except:
        print("Stop invalid")
        sys.exit(1)
    res = urllib.request.urlopen(url4)
    data =res.read()
    file = open("stop.json",'wb')
    file.write(data)

    json_data = json.loads(data)
    data1 = json_data[0]
    data2 = json.dumps(data1)
    json_data = json.loads(data2)
    print(json_data['DepartureText'])
except:
    print("No available bus")
    sys.exit(1)
