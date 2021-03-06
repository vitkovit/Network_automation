from netmiko import ConnectHandler
import yaml
import ipaddress
import getpass


########################## define commands ##########################
COMMANDS = ["show running-config", "copy running-config startup-config"]                       # for "wr" there is no expected output, so good trick
########################## define commands ##########################

with open ('inventory_02.yml') as yaml_file:                                                   # use with open because file is automaticaly closed
    yaml_content = yaml.safe_load(yaml_file)                                                   # define global dictionary yaml_content

def credentials():                                                                             # will define username and password
    ssh_username = input("SSH username: ")
    ssh_password = getpass.getpass('SSH Password: ')
    credentials_used = {'username':ssh_username,'password':ssh_password}
    return credentials_used

def device_data(open_file,stored_credentials):
    for device in open_file['all']['sites']['hosts']:
        device_in_site = {}                                                                     # populate list for connecting
        device_in_site.update({'device_type':(open_file['all']['sites']['device_type_cisco'])})
        ip_address = ipaddress.IPv4Interface(open_file['all']['sites']['hosts'][device]['ip'])
        device_in_site.update({'host':str(ip_address.ip)})                                      # convert to str because it is <class 
        device_in_site.update(stored_credentials)                                               # update dictionary with credentials from another function

        ip_interface = open_file['all']['sites']['hosts'][device]['interfaces']                 # extract "interfaces" value of nested dictionary
        lo_address = str(ipaddress.IPv4Interface(ip_interface["lo0"]).ip)                       # split ip part an make it as string
        lo_mask = str(ipaddress.IPv4Interface(ip_interface["lo0"]).netmask)                     # split CIDR, convert it to netmask as string
        config_loopback = ["interface lo0", "ip address "+lo_address+" "+lo_mask,"wr"]          # create strings for configuration line, "," means new line

        con_device = ConnectHandler(**device_in_site)                                           # connect to each device
        output = con_device.send_config_set(config_loopback)                                    # config loopback interface with set of commands
        save_config = con_device.send_command(COMMANDS[1], expect_string=r'Destination filename')       #expected string to continue wit saving to flash
        con_device.disconnect()

        print(f"device: {device}, lo0 IP: {lo_address} {lo_mask}")                              # print what is configured

device_data(yaml_content,credentials())                                          # call function with parameters of yaml dictionary and what ever is returned by 
