import socket

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
    
    
