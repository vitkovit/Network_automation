#%% 
# import pyping

r = pyping.ping('google.com')

if r.ret_code == 0:
    print("Success")
else:
    print("Failed with {}".format(r.ret_code))
#%%
# https://forum.huawei.com/enterprise/en/python-ping-many-devices-with-1-simple-script/thread/627581-871
import subprocess
def ping_test (host):

    reached = []                           #Empty list to collect reachable hosts
    not_reached = []                          #Empty list to collect unreachable hosts

    for ip in host:
        ping_test = subprocess.call('ping %s -n 2' % ip)        #Ping host n times
        if ping_test == 0:                    #If ping test is 0, it' reachable
            reached.append(ip)

        else:
            not_reached.append(ip)                              #Else, it's not reachable

    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))
hosts = ["192.168.1.1","123.214.2.2","www.google.com",]         #Hosts list
ping_test (hosts)
#%%
import os
from time import sleep

def add():
    print("in add function")

def sub():
    print("in subtract function")

def ping():
    online = os.system("ping -n 1 8.8.8.8")
    if(online == 0):
         print("Avilabe with ",online)
         return True
    else:
         print("Ofline with ",online)
         return False

while True:
   add()
   sleep(0.5)
   if( ping()):
         sub()
#    do other things if ping is successful
   sleep(0.5)

#%%
# https://www.geeksforgeeks.org/build-a-gui-application-to-ping-the-host-using-python/
# import modules
from tkinter import *
from pythonping import ping
 
def get_ping():
    result = ping(e.get(), verbose=True)
    res.set(result)
 
# object of tkinter
# and background set for light grey
master = Tk()
master.configure(bg='light grey')
 
# Variable Classes in tkinter
res = StringVar()
 
# Creating label for each information
# name using widget Label
Label(master, text="Enter URL or IP :",
      bg="light grey").grid(row=0, sticky=W)
Label(master, text="Result :", bg="light grey").grid(row=1, sticky=W)
 
# Creating lebel for class variable
# name using widget Entry
Label(master, text="", textvariable=res, bg="light grey").grid(
    row=1, column=1, sticky=W)
 
e = Entry(master)
e.grid(row=0, column=1)
 
# creating a button using the widget
# Button that will call the submit function
b = Button(master, text="Show", command=get_ping)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)
 
mainloop()

#%%
import os
hostname = "8.8.8.8" #example
response = os.system("ping " + hostname)
#response = os.popen(f"ping -c 1 " + hostname)

#input("press key...")
#and then check the response...
if response == 0:
  print(f"{hostname} is up!")
else:
  print(f"{hostname} is down!")

  
#%% V01
import subprocess
def ping_test (host):

    reached = []                           #Empty list to collect reachable hosts
    not_reached = []                          #Empty list to collect unreachable hosts

    for ip in host:
        #ping_test = subprocess.call('ping %s -n 2' % ip).       #Ping host n times
        ping_test = subprocess.check_output(f"ping {ip}")
# you see this is silly because it will return class 'bytes' so you need to to all kind of mumbo-jumbo to translate to form you want
        print(ping_test.translate(None, b'\n').decode().split("\r"))
        #print(ping_test.translate.decode('\r\n'))
        if ping_test == 0:                    #If ping test is 0, it' reachable
            reached.append(ip)
        else:
            not_reached.append(ip)                              #Else, it's not reachable
#interface_config.split("\n")
    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))
hosts = ["10.0.0.101","10.0.0.102","10.0.0.103","10.0.0.104","10.0.0.105","10.0.0.106","10.0.0.107","10.0.0.109",]         #Hosts list
ping_test (hosts)