# -*- coding: UTF-8 -*-
import socket               
 
s = socket.socket()        
host = socket.gethostname() 
port = 12345           
 
s.connect((host, port))
print "\033[30m已接受\033[0m"
print s.recv(1024)
s.close()
