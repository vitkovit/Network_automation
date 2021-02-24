from netmiko import ConnectHandler
import yaml
import datetime
import os
import ipaddress
import getpass


########################## define time ##########################
def time_function():
    filename = datetime.datetime.now()
    TIME=filename.strftime("%d_%m_%Y_%H-%M-%S")
    return TIME
                                
########################## define time ##########################
########################## define fodlers ##########################
folders=["Config archive", "example"]                       # list of directory you want to create
FOLDER=folders[0]                                           # select witch folder should be created
try:
    os.mkdir(FOLDER)
except FileExistsError:                                     #if file exist python will show "FileExistsError:" error
    print("folder exist: %s" % FOLDER)
else:
    print("Directory created: %s" % FOLDER)    
########################## define fodlers ##########################

########################## define commands ##########################
COMMANDS = ["show running-config"]
########################## define commands ##########################

with open ('inventory_02.yml') as yaml_file:                                                   # use with open because file is automaticaly closed
    yaml_content = yaml.safe_load(yaml_file)                                                   # define global dictionary yaml_content

def credentials():                                                                             # will define username and password
    ssh_username = input("SSH username: ")
    ssh_password = getpass.getpass('SSH Password: ')
    credentials_used = {'username':ssh_username,'password':ssh_password}
    return credentials_used

def device_data(open_file,stored_credentials,defined_time):
    for device in open_file['all']['sites']['hosts']:
        device_in_site = {}
        device_in_site.update({'device_type':(open_file['all']['sites']['device_type_cisco'])})
        ip_address = ipaddress.IPv4Interface(open_file['all']['sites']['hosts'][device]['ip'])
        device_in_site.update({'host':str(ip_address.ip)})                                      # convert to str because it is <class 
        device_in_site.update(stored_credentials)                                               # update dictionary with credentials from another function

        con_device = ConnectHandler(**device_in_site)
        output = con_device.send_command(COMMANDS[0])
        with open(f"{FOLDER}/{device}_{defined_time}.txt", "w") as file_to_save:                # format, anc "w"(create file if does not exist)
            file_to_save.close()
        con_device.disconnect()

device_data(yaml_content,credentials(),time_function())                                          # call function with parameters of yaml dictionary and what ever is returned by credentials 
