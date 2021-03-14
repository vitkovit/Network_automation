from netmiko import ConnectHandler
import yaml
import ipaddress
import getpass
import csv


with open ('inventory_02.yml') as yaml_file:                                                   # use with open because file is automaticaly closed
    yaml_content = yaml.safe_load(yaml_file)                                                   # define global dictionary yaml_content
    #print(yaml_content)
for device in yaml_content['all']['sites']['hosts']:
    #return device
    with open('config_data.csv', 'a', newline='\n') as csv_file:
        csv_file.write(device+ "\n")