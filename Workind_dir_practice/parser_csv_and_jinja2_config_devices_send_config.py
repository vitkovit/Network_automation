import csv
from jinja2 import Template
import pandas as pd
import numpy as np
from netmiko import ConnectHandler
import yaml
import ipaddress
import getpass


csv_source = "config_data.csv"
jinja2_source = "template_interface_types.j2"
yaml_source = "inventory_02.yml"
COMMANDS = ["show running-config", "copy running-config startup-config"]                       # for "wr" there is no expected output, so good trick

def credentials():                                                                             # will define username and password
    ssh_username = input("SSH username: ")
    ssh_password = getpass.getpass('SSH Password: ')
    credentials_used = {'username':ssh_username,'password':ssh_password}
    return credentials_used

with open (yaml_source) as yaml_file:                                                   # use with open because file is automaticaly closed
#    yaml_content = yaml.safe_load(yaml_file)       
    open_file = yaml.safe_load(yaml_file) 

with open(jinja2_source) as jinja2file:
# keep_trailing_newline=True is used to add empty line between each configuration
    interface_type_template = Template(jinja2file.read(), keep_trailing_newline=True)

# read file reader with panda, but read as csv
fill_reader = pd.read_csv("config_data.csv")                               
# convert "vlan" column to integer type with numpy, if not, vlan will be 999.0 (float)
fill_reader["vlan"] = np.nan_to_num(fill_reader["vlan"]).astype(int)
# read "device" column and fill empty spaces with value of first field
fill_reader["device"] = fill_reader["device"].fillna(method='ffill')
# every empty field will habe NaN in it, so replace this with "" (empty) value
fill_reader = fill_reader.replace(np.nan, "")

# convert fill_reader to dictionary ‘records’ will list in form [{column -> value}, ...]
converted_data_csv = fill_reader.to_dict(orient='records')
interface_configs = ""

def command_list(csv_data,jinja2_int_template,yaml_data): ##,yaml_data,stored_credentials
    return_values = []
    for device in yaml_data['all']['sites']['hosts']:
        for row in csv_data:
        #for every row in csv file render it with jinja2 template
            interface_config = jinja2_int_template.render(
                local_intr = row["local-intr"],
                next_device = row["next-device"],
                remote_intr = row["remote-intr"],
                channel_number = row["channel-number"],
                vlan = row["vlan"],
                po_mode = row["po-mode"],
                #just for funn add comment to know on witch device configuration is happening
                device_name = row["device"]
            )

            if row["device"] == device:
                return_values.append(interface_config.split("\n"))

    return return_values
    #return return_values
    #return return_values
                #return interface_config.split("\n")
            
"""
def device_data():
    for device in yaml_data['all']['sites']['hosts']:
    #if row["device"] == device:
        device_in_site = {}                                                                     # populate list for connecting
        device_in_site.update({'device_type':(open_file['all']['sites']['device_type_cisco'])})
        ip_address = ipaddress.IPv4Interface(open_file['all']['sites']['hosts'][device]['ip'])
        device_in_site.update({'host':str(ip_address.ip)})                                      # convert to str because it is <class 
        device_in_site.update(stored_credentials)
        print(device_in_site)
"""
        #interface_configs += interface_config
    #TBC.... need to make condition for connecting to the device
        #if row["device"] == "CORE_01":
        #print(interface_config)
        #print(row["device"])# == open_file['all']['sites']['hosts']:
"""        for device in yaml_data['all']['sites']['hosts']:
            if row["device"] == device:
                device_in_site = {}                                                                     # populate list for connecting
                device_in_site.update({'device_type':(open_file['all']['sites']['device_type_cisco'])})
                ip_address = ipaddress.IPv4Interface(open_file['all']['sites']['hosts'][device]['ip'])
                device_in_site.update({'host':str(ip_address.ip)})                                      # convert to str because it is <class 
                device_in_site.update(stored_credentials)
                print(device_in_site)
                print(interface_config.split("\n"))
"""
                #print(interface_config.split("\n"))
                #save_config = con_device.send_command(COMMANDS[1], expect_string=r'Destination filename')       #expected string to continue wit saving to flash
                #con_device.disconnect()
"""
        for device in yaml_data['all']['sites']['hosts']:
            if row["device"] == device:
                #print(device)
                #print(row["device"])
                #print(yaml_data['all']['sites']['hosts'][device]["ip"])
                #print(interface_config.split("\n"))
                device_in_site = {}                                                                     # populate list for connecting
                device_in_site.update({'device_type':(open_file['all']['sites']['device_type_cisco'])})
                ip_address = ipaddress.IPv4Interface(open_file['all']['sites']['hosts'][device]['ip'])
                device_in_site.update({'host':str(ip_address.ip)})                                      # convert to str because it is <class 
                device_in_site.update(stored_credentials)   
                #print(device_in_site)
                #print(interface_config.split("\n"))



                #con_device = ConnectHandler(**device_in_site)                                           # connect to each device
                #output = con_device.send_config_set(interface_config.split("\n"))                                    # config loopback interface with set of commands
                print(device_in_site)
                #print(interface_config.split("\n"))
                #save_config = con_device.send_command(COMMANDS[1], expect_string=r'Destination filename')       #expected string to continue wit saving to flash
                #con_device.disconnect()
"""
                #print(f"connecting to: {device}, IP: {ip_address}")    
        #if row["device"] == open_file['all']['sites']['hosts']:
            #print(row["device"])
        #print(device)
#    print(row)
    #with open("interface_configs.txt", "w") as f:
    #    f.write(interface_configs)
 #   config_set = interface_configs.split("\n") # this will split to every new line as a list
 #   print(config_set)

def device_config(yaml_data,stored_credentials):
    for device in yaml_data['all']['sites']['hosts']:
        #print(device)
        #print(row["device"])
        #print(yaml_data['all']['sites']['hosts'][device]["ip"])
        #print(interface_config.split("\n"))
        device_in_site = {}                                                                     # populate list for connecting
        device_in_site.update({'device_type':(open_file['all']['sites']['device_type_cisco'])})
        ip_address = ipaddress.IPv4Interface(open_file['all']['sites']['hosts'][device]['ip'])
        device_in_site.update({'host':str(ip_address.ip)})                                      # convert to str because it is <class 
        device_in_site.update(stored_credentials)   
        #print(device_in_site)
        return device_in_site

        #print(interface_config.split("\n"))


def device_connect(test):
    print(test)
        #con_device = ConnectHandler(**device_in_site)                                           # connect to each device
        #output = con_device.send_config_set(interface_config.split("\n"))                                    # config loopback interface with set of commands
        #print(interface_config.split("\n"))
        #save_config = con_device.send_command(COMMANDS[1], expect_string=r'Destination filename')       #expected string to continue wit saving to flash
        #con_device.disconnect()
"""
for device in open_file['all']['sites']['hosts']:
    if device == 
    print(device)
"""
x= command_list(converted_data_csv,interface_type_template,open_file) #,credentials()
y= device_config(open_file,credentials())
#device_connect(y)
print(y)

#print(type(command_list(converted_data_csv,interface_type_template,open_file))) #,credentials()
