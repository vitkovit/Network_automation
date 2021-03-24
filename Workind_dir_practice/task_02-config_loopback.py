from netmiko import ConnectHandler
import yaml
import datetime
import os

filename = datetime.datetime.now()
TIME=filename.strftime("%d_%m_%Y_%H-%M-%S")

my_inventory = open('inventory_01.yml').read()                  # read yaml file .r is not working
my_inventory_yaml = yaml.safe_load(my_inventory)                # readed output saved as variable
for site_dict in my_inventory_yaml["all"]["sites"]:            # this will check dictionary under key "all" and list "sites"
    for host in site_dict["hosts"]:
        host_dict = {}                                          # define empty dictionary
        host_dict.update({'device_type': 'cisco_ios'})          # update host_dict dic what is not in yaml file
        host_dict.update(my_inventory_yaml["all"]["vars"])      # update host_dict dic with login credentials
        for key, value in host.items():
            interface_config=[]                                 # define empty list
            ip_list = value['ip'].split('/')[0]                 # strip CIDR and leave clean IP
            ip_key=dict.fromkeys({'ip'})                        # create dictionary key "IP"
            ip_key['ip']=ip_list                                # assign IP as value for key 'ip'
            host_dict.update(ip_key)                            # updare host_dict with values "username" and "password" from YAML file
            int_lo_address=(value["interfaces"]["lo0"]+' '+value["interfaces"]["netmask"])      # create string with IP and MASK
            interface_config=["interface lo0", "ip address "+int_lo_address]                    # create string with lo0 + ip
            for devices in host:
                device_name = devices

            device = ConnectHandler(**host_dict)                # netmiko connect handler calling host_dict
            output = device.send_config_set(interface_config)   # sendig predefined list of configuration
            device.disconnect()                                 # close connection
            print("loopback lo0 created with IP: {} on device: {}".format(int_lo_address,device_name))


