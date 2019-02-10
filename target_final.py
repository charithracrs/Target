import sys
import urllib2, json

route = sys.argv[1]
stop = sys.argv[2]
direction = sys.argv[3]
'''
#print('Route = ')
route = "30 - Broadway Crosstown - Westgate Station"
stop = "Golden Valley Rd and Xerxes Ave"
direction = "east"
'''

#print(route, stop, direction)

url1 = "http://svc.metrotransit.org/NexTrip/Routes?format=json"

#res = urllib.request.urlopen(url1)
res = urllib2.urlopen(url1)
data =res.read()
file = open("route.json",'wb')
file.write(data)
json_data = json.loads(data)

#print(json_data)
#print(type(json_data))

for item in json_data:
    if(item['Description'] == route ):
        #print('Route=',item['Description'])
        #print('Route no.=', item['Route'])
        route_num = item['Route']

url2 = "http://svc.metrotransit.org/NexTrip/Directions/"+route_num+"?format=json"
res = urllib2.urlopen(url2)
data =res.read()
file = open("direction.json",'wb')
file.write(data)
json_data = json.loads(data)
#print(json_data)
for item in json_data:
    #print(item['Text'])
    dirc = item['Text']
    if(direction.lower() in dirc.lower()):
        #print("Direction=",dirc)
        dir_num = item['Value']

url3 = "http://svc.metrotransit.org/NexTrip/Stops/"+route_num+"/"+dir_num+"?format=json"
res = urllib2.urlopen(url3)
data =res.read()
file = open("stop.json",'wb')
file.write(data)
json_data = json.loads(data)

for item in json_data:
    if(item['Text'] == stop):
        #print(item['Text'])
        #print(item['Value'])
        stop_num = item['Value']

url4 = "http://svc.metrotransit.org/NexTrip/"+route_num+"/"+dir_num+"/"+stop_num+"?format=json"
res = urllib2.urlopen(url4)
data =res.read()
file = open("stop.json",'wb')
file.write(data)
json_data = json.loads(data)
data1 = json_data[0]
data2 = json.dumps(data1)
json_data = json.loads(data2)
print(json_data['DepartureText'])
