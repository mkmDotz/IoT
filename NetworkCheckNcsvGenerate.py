import socket
import csv
import random
import time

def sensorData():
    for i in range (1,101): # Unexpected Error.. Not working for range(1,101):(

        data = [time.time(), i , random.randint(1,9),random.randint(10,99)]
        out.writerow(data)
        out.writerow("\n")

    
REMOTE_SERVER = "www.google.com"
def is_connected():
  try:
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False


if(is_connected()):
    print("Sensor data is getting Updated in HCP")
    
else:
    print("Create CSV file to store Sensor Data")
           
    headers = ["DateTime", "Sensor1", "Sensor2", "Sensor3"]
    #out = csv.writer(open("testNew.csv","w"), delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
    #out = csv.writer(open("Test.csv","w"),delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    out = csv.writer(open("Test1.csv","w"),delimiter=' ')
    out.writerow([headers])
    out.writerow([sensorData()])
