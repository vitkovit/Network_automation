# %% MISS ping script, but it is bad because response value
import os
def ping_test (host):
    for ip in host:
        response = os.system("ping -n 1 " + ip)
        print(response)
        if response == 0:
            print(f"{ip} is up!")
        else:
            print(f"{ip} is down!")

hosts = ["10.0.0.101","10.0.0.102","10.0.0.103","10.0.0.104","10.0.0.105","10.0.0.106","10.0.0.107","10.0.0.109",]         #Hosts list
ping_test (hosts)

# %% lets go more pro xD 

import os
def ping_test (host):

    for ip in host:
# popen is just pipe that will see what is in putput
# looks like this: os.popen(command[, mode[, bufsize]])
# dont forget that popen2,3,4 are not available in python3, it use subprocess module with .call, that is similar 

        # lets ping only 2 times to be faster
        response = os.popen(f"ping {ip} -n 2").read() # dont forget to read it, 
        #print(response) # this will print out output from csd
        # include whatever you want to match in response output, be careful for false positive, so dont include "Received = 2" because "Destination net unreachable" also contains the same string
        if "bytes" and "time" and "TTL" in response:
            print(f"{ip} is reachable")
        else:
            print(f"can't reach {ip}")
# create host list, later we will upload it from YAML file
hosts = ["10.0.0.101","10.0.0.102","10.0.0.103","10.0.0.104","10.0.0.105","10.0.0.106","10.0.0.107","10.0.0.109",]

ping_test (hosts)
# %% Now lets include threads
import os
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
def ping_test(host):

    for ip in host:
        response = os.popen(f"ping {ip} -n 2").read() # dont forget to read it, 
        #print(response)
        if "bytes" and "time" and "TTL" in response:
            print(f"{ip} is reachable")
        else:
            print(f"can't reach {ip}")
# host list needs to be modified, map function wil go throug list but it will split ip addresses by each charachter, becausse format is str, so you need to have list of multiple lists
hosts = [['10.0.0.101'],['10.0.0.102'],['10.0.0.103'],['10.0.0.104'],['10.0.0.105'],['10.0.0.106'],['10.0.0.107'],['10.0.0.108'],['10.0.0.109']]

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(ping_test, hosts)
# keep in mid that output will not be ordered, but that is normal because some threads are faster, some slower
# also see how print function suck as output, in next example we will use logging module

# %%
import os

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import threading
def ping_test(host):

    for ip in host:
        response = os.popen(f"ping {ip} -n 4").read() # dont forget to read it, 
        #print(response)
        if "bytes" and "time" and "TTL" in response:
            print(f"{ip} is reachable")
            #time.sleep(1)
        else:
            print(f"can't reach {ip}")
#hosts = ["10.0.0.101","10.0.0.102","10.0.0.103","10.0.0.104","10.0.0.105","10.0.0.106","10.0.0.107","10.0.0.109",]
hosts = [['10.0.0.101'],['10.0.0.102'],['10.0.0.103'],['10.0.0.104'],['10.0.0.105'],['10.0.0.106'],['10.0.0.107'],['10.0.0.109']]
#print(len(hosts))
#for x in hosts:
#    print(type(x))
thread_list = []
for host in hosts:
    #print(type(host))

# to thread, add and argument list, this will fill function argument
    threads = threading.Thread(target=ping_test, args=host)
    threads.start()
    thread_list.append(threads)

#for thread in thread_list:
#    thread.join()




    
# %%
import os
from concurrent.futures import ThreadPoolExecutor
import logging
from datetime import datetime

# now this logging module has a lot to learn from, main thing is that is trusted to map msg level to thread
# so lets define format for logging, this is basicaly the bone structure of message that will go infront of our custom msg that we wil ldefine later 

logging.basicConfig(format = '%(thread)d - %(name)s - %(levelname)s %(message)s', level=logging.INFO)

# now this is just a format to write it, depending on print style, latter on ".format" will be used so by default "%" is used, and ")s" to mark type of data
# for example "%(created)f" is float type, and so on, like "%(thread)d" is Decimal integer,
# so if you reeealy want to know thread ID, you can have it (don't know why, but still xD)
# leve is one of 6 types, other type could be ERROR or CRITICAL
# one more thing !!!IMPORTANT, you must include "%(message)s" if you want to print custom msg later in code 
def ping_test(host):

    for ip in host:
        response = os.popen(f"ping {ip} -n 2").read() 
        # so lets define format for send and received messages, this will write after logging msg
        # create firs msg variable with 2 placeholders, one will be for time, second for iterrator
        send_msg = ': {} ping to {}'
        # create second variable with 2 placeholders
        received_msg = ': {} responde from {}'
        # now format first msg, start with root logger ".info" msg, this will type in "%(levelname)s" what type of msg it is, in this case it will be "INFOR", if you put ".critical" it will output "CRITICAL", and so on, format for this is "logging.info(msg, *args, **kwargs)"
        # define variable "send_msg" from before, now format it, since we have placeholders in variables, we need to use str.format, in the first placeholder it will go (time), second is (iterrator)
        # if you dint specified variables with placeholders, in one line it would look like:
            # logging.info(': {} ping to {}'.format(datetime.now().strftime("%H:%M:%S"), ip))
        # got it? or like this:
            #logging.info(f': {datetime.now().strftime("%H:%M:%S")} ping to {ip}')
        # whatever floats your boat xD 
        # for first variable, take current time, novert it to stingformat using ".strftime", if you dont want it too long, format tit with %H:%M:%S
        logging.info(send_msg.format(datetime.now().strftime("%H:%M:%S"), ip))
        if "bytes" and "time" and "TTL" in response:
            # if condition match, ip is pingable and return some msg
            logging.info(received_msg.format(datetime.now().strftime("%H:%M:%S"), ip))
        else:
            # for fun, lets add warning in this format, it will be obvious that ip is not responding 
            logging.info(received_msg.format(datetime.now().strftime("%H:%M:%S"), ip) + f"\n!WARNING! can't reach {ip}")
# host list needs to be modified, map function wil go throug list but it will split ip addresses by each charachter, becausse format is str, so you need to have list of multiple lists
hosts = [['10.0.0.101'],['10.0.0.102'],['10.0.0.103'],['10.0.0.104'],['10.0.0.105'],['10.0.0.106'],['10.0.0.107'],['10.0.0.108'],['10.0.0.109']]

#with ThreadPoolExecutor(max_workers=8) as executor:
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(ping_test, hosts)
# keep in mid that output will nob be ordered, lets fix this
# %% now this list looks silly, lets read it from yaml file... TBC

