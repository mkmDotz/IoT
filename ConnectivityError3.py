import socket
import csv
import random
import datetime



REMOTE_SERVER = "www.google.com"

header = ["TimeStamp" , "Temp Sensor","Ultrasonic Sensor"],
data = [
    [datetime.datetime.now(),29.9, 1.25]
]

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
           
    with open('Test.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(data)

    
