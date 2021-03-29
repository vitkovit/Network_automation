import csv
from jinja2 import Template
import pandas as pd
import numpy as np
from netmiko import ConnectHandler
import yaml
import ipaddress
import getpass
import concurrent.futures
from itertools import chain
from collections import defaultdict


csv_source = "config_data.csv"
jinja2_source = "template_interface_types.j2"
yaml_source = "inventory_02.yml"
COMMANDS = ["show running-config", "copy running-config startup-config", "wr"]  
# for "wr" there is no expected output, so good trick

def credentials():                                                    # will define username and password
    ssh_username = input("SSH username: ")
    ssh_password = getpass.getpass('SSH Password: ')
    credentials_used = {'username':ssh_username,'password':ssh_password}
    return credentials_used

with open (yaml_source) as yaml_file:                                 # use with open because file is automaticaly closed
    open_yaml_file = yaml.safe_load(yaml_file) 

with open(jinja2_source) as jinja2file:
    interface_type_template = Template(jinja2file.read(), keep_trailing_newline=True)
# keep_trailing_newline=True is used to add empty line between each configuration

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


def connections(yaml_data,stored_credentials,configuration_for_device):
    for device in yaml_data['all']['sites']['hosts']:
        device_in_site = {}                                     # populate list for connecting
        device_in_site.update({'device_type':(yaml_data['all']['sites']['device_type_cisco'])})
        ip_address = ipaddress.IPv4Interface(yaml_data['all']['sites']['hosts'][device]['ip'])
        device_in_site.update({'host':str(ip_address.ip)})       # convert to str because it is <class 
        device_in_site.update(stored_credentials)
        #yield device_in_site
        #command_list(device)
        #command_list(converted_data_csv,interface_type_template,device)
        #connect_config(**device_in_site)
        #connect_config(device_in_site)
        #return device_in_site
        if device in configuration_for_device:
            #print(configuration_for_device[device])
            print(f"Connecting to: {device}")
            #print(f"sending config: {configuration_for_device[device]}")
            con_device = ConnectHandler(**device_in_site)
            output = con_device.send_config_set(configuration_for_device[device])
            print(output)
            input("Press Enter to continue...")
            con_device.disconnect
#print(type(x))

def command_list(csv_data,jinja2_int_template):
    interface_config_set = {}
    configuration_dictionary = defaultdict(list)
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
        return_values = []
        return_values += interface_config.split("\n")
        interface_config_set[row["device"]] = return_values
        for device_names in interface_config_set.keys():
            if device_names == row["device"]:
                configuration_dictionary[device_names].append(return_values)
    #print(configuration_dictionary)
    return configuration_dictionary


connections(open_yaml_file,credentials(),command_list(converted_data_csv,interface_type_template))
#command_list(converted_data_csv,interface_type_template,command_list(converted_data_csv,interface_type_template))
"""
with concurrent.futures.ThreadPoolExecutor() as exe:
    configuration_for_device = command_list(converted_data_csv,interface_type_template)
    results = exe.map(connections, open_yaml_file, credentials(), configuration_for_device)
"""
#def connections(yaml_data,stored_credentials,configuration_for_device):

"""
def connect_config(device_to_connect,configuration_for_device):
        con_device = ConnectHandler(**device_to_connect)
        output = con_device.send_config_set(configuration_for_device)
        input("Press Enter to continue...")
        con_device.disconnect
"""

#command_list(converted_data_csv,interface_type_template,x)
#x = connections(open_yaml_file,credentials())
#z = command_list(converted_data_csv,interface_type_template,x)

#y = map(connect_config(x,z))
"""
def command_list(csv_data,jinja2_int_template,yaml_data,stored_credentials):




    for device in yaml_data['all']['sites']['hosts']:           # this will iterate through device list from YAML file

        with concurrent.futures.ThreadPoolExecutor() as exe:
            results = exe.map(x)


            device_in_site = {}                                     # populate list for connecting
            return_values = []                                      # create list of config separated \n with ","
            for row in csv_data:                                    # iterate through each row
                interface_config = jinja2_int_template.render(      # Jinja2 will use this as variables in template
                    local_intr = row["local-intr"],
                    next_device = row["next-device"],
                    remote_intr = row["remote-intr"],
                    channel_number = row["channel-number"],
                    vlan = row["vlan"],
                    po_mode = row["po-mode"],
                    #just for fun add comment to know on witch device configuration is happening
                    device_name = row["device"]
                    )

                # compare if device name in YAML file match device name in CSV row                    
                if device == row["device"]:
                    # if they match, add each line of populated jinja template to the list, but only for current device in first "for" function, also separeate each new line and split with "," in the list, that way "send_config_set" function can read the whole list for each device
                    return_values += interface_config.split("\n")


            # device_in_site dictionary is now populating data for "ConnectHandler"
            device_in_site.update({'device_type':(yaml_data['all']['sites']['device_type_cisco'])})
            ip_address = ipaddress.IPv4Interface(yaml_data['all']['sites']['hosts'][device]['ip'])
            device_in_site.update({'host':str(ip_address.ip)})       # convert to str because it is <class 
            device_in_site.update(stored_credentials)                # laod credentials from another function

            print(f"Connecting to: {device}")                        # check in witch device will script connect
            con_device = ConnectHandler(**device_in_site)            # connect to each device
            # for each device, the whole list "return_values" is send to configure
            output = con_device.send_config_set(return_values)
            #print(output)                                           # for reding output to the device
            #input("Press Enter to continue...")                     # for pausing between devices because terminal is too short

            save_config = con_device.send_command(COMMANDS[1], expect_string=r'Destination filename')       #expected string to continue wit saving to flash
            save_config_wr = con_device.send_command(COMMANDS[2])       # for good measure MISS
            con_device.disconnect



x = command_list(converted_data_csv,interface_type_template,open_yaml_file, credentials())



with concurrent.futures.ThreadPoolExecutor() as exe:
    results = exe.map(x)


    
    with cf.ThreadPoolExecutor(max_workers=5) as ex:
        ex.map(connect_device, device_data)

"""