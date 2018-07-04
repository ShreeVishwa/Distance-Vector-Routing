import socket         
import sys
import json
import os      

filename = sys.argv[1]
host = filename.split('.')[0]
hostname = sys.argv[2]

s = socket.socket()         
# print "Socket successfully created"

port = 12345   
print "hostname is",hostname            

# print "host is ", host
s.bind((hostname, port))        
# print "socket binded to %s" %(port)

# put the socket into listening mode
s.listen(5)     
# print "socket is listening"           

try:
    while True:

       # Establish connection with client.
       c, addr = s.accept()     
       # print 'Got connection from', addr
       distance_vector = {}
       fp = open(filename,'r')
       for line in fp:
           data = line.split(',')
           if data[1] == 'inf':
               data[1] = sys.maxint
           distance_vector[data[0]] = (data[1],data[2][:-1])

       c.send(json.dumps(distance_vector))
       c.close()
except:
    s.close()