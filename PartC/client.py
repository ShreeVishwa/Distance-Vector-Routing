import socket
import os
import sys
import json     
import time

def bellman_ford(new_data,new_node,old_data):
    # print "I am good"
    # print "old data in finc is ",old_data
    updated_data = {}
    
    for key in old_data:
        
        # print "I am in"
        # print key
        # print old_data[key][0]
        # if new_data[key][0]:
        #     print type(int(new_data[key][0]))
        # if old_data[key][0]:
        #     print type(int(old_data[key][0]))
        # if new_data[new_node][0]:
        #     print type(int(new_data[new_node][0]))
        # print "new_data is ", new_data
        # print "old_data is ", old_data
        # print "old_node is ", new_node
        # print "new_data[key]",
        # print int(new_data[key][0])
        # print "new_data[old_node]",
        # print int(new_data[new_node][0])
        # print "old_data[key]",
        # print int(old_data[key][0])
        if int(new_data[key][0]) > (int(new_data[new_node][0]) + int(old_data[key][0])):
            # print "yes",int(new_data[key][0]),(int(new_data[new_node][0]) + int(old_data[key][0]))
            # print int(new_data[new_node][0]),int(old_data[key][0])
            # print new_data[new_node][0],old_data[key][0]
            # print "updated_sum is ",int(new_data[new_node][0]) + int(old_data[key][0])
            updated_data[key] = [int(new_data[new_node][0]) + int(old_data[key][0]),new_data[key][1]]
            # print updated_data
            # new_data[key][0] = (new_data[new_node][0] + old_data[key][0])
        else:
            # print " same sum is ",new_data[key][0]
            updated_data[key] = [new_data[key][0],new_data[key][1]]
        
    
    # print updated_data
    return updated_data   
    # return 0           

filename = sys.argv[1]
host = filename.split('.')[0]


# Define the port on which you want to connect
port = 12345   
s_time = time.time()          

while True:

    distance_vector = {}
    fp = open(filename,'r')
    neighbours = []
    for line in fp:
        data = line.split(',')
        if data[1] == 'inf':
            data[1] = sys.maxint
        if data[2][:-1] != "" and data[0] != host:
            neighbours.append((data[2][:-1],data[0]))
        distance_vector[data[0]] = (int(data[1]),data[2][:-1])

    # Create a socket object
    for ip in neighbours:
        s = socket.socket()   
        # connect to the server on local computer 
        print ip[0]  
        s.connect((ip[0], port))  

        # print "json data is ",json.loads(s.recv(2048))
        # receive data from the server
        rev_data = json.loads(s.recv(2048))
        new_data = distance_vector
        new_node = host
        old_node = ip[1]
        print "old_node is ", old_node
        # print " Old data is " ,rev_data
        old_data = {}
        for key in rev_data:
            old_data[str(key)] = rev_data[str(key)]
        # print "old data is ", old_data
        # print "New data is ", new_data
        updated_table = bellman_ford(new_data,old_node,old_data)
        # print "updated table is ",updated_table
        # print "new table is ",new_data
        new_weights = []
        old_weights = []
        for key in updated_table:
            new_weights.append(updated_table[key][0])
            old_weights.append(new_data[key][0])
        print new_weights
        print old_weights
        if new_weights != old_weights:
            # print "yes"
            # print updated_table
            # e_time = time.time()
            fp = open(filename,'w')
            # for key in updated_table:
            #     print key
            for key in updated_table:
                # print "hello",key
                if updated_table[key][0] == sys.maxint:
                    fp.write(key+",inf,"+updated_table[key][1]+"\n")
                # +updated_table[key][0]+","+updated_table[key][1]+"\n"
                else:
                    fp.write(key+","+str(updated_table[key][0])+","+updated_table[key][1]+"\n")
                # print "successfully written to",host
        fp.close()
        # print "start_time is",s_time
        # print "end_time is ",e_time
        # close the connection
        s.close()