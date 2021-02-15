"""from netmiko import ConnectHandler
from datetime import datetime
from copy import deepcopy
import yaml

SH_COMMANDS = ["show running-config"]

def read_yaml(path="inventory_01.yml"):
    with open(path) as f:
        yaml_content = yaml.safe_load(f.read())
    return yaml_content

def get_connection_parameters(parsed_yaml):
    parsed_yaml = deepcopy(parsed_yaml)
    login_credentials = parsed_yaml["all"]["vars"]
    for site_dict in parsed_yaml["all"]["sites"]:
        for host in site_dict["hosts"]:
            host_dict = {}
            host_dict.update(login_credentials)
            host_dict.update(host)
            yield host_dict

def show_commands(devices, commands):
    for device in devices:
        start_time = datetime.now()
        hostname = device.pop("name")
        connection = ConnectHandler(**device)
        device_result = ["{0} {1} {0}".format("=" * 15, hostname)]

        for command in commands:
            command_result = connection.send_command(command)
            device_result.append("{0} {1} {0}".format("=" * 10, command))
            device_result.append(command_result)

        device_result_string = "\n\n".join(device_result)
        connection.disconnect()
        device_result_string += "\nElapsed time: " + str(datetime.now() - start_time)
        yield device_result_string

def main():
    parsed_yaml = read_yaml()
    print(parsed_yaml)
    connection_parameters = get_connection_parameters(parsed_yaml, site_name=SITE_NAME)

    for device_result in show_commands(connection_parameters, SH_COMMANDS):
        print(device_result)


if __name__ == "__main__":
    main()

"""


from netmiko import ConnectHandler
import yaml
#with open("inventory_01.yml") as f:
#    my_inventory=yaml.safe_load(f)
#def output_ip():
my_inventory = open('inventory_01.yml').read()              # read yaml file .r is not working
my_inventory_yaml = yaml.safe_load(my_inventory)            # readed output saved as variable
#print(type(my_inventory_yaml))                              # variable is a DICT
#print(type(my_inventory_yaml["all"]))                       # this is DICT
#print(my_inventory_yaml["all"])                              # this will print whole dictionary "all"
#print(type(my_inventory_yaml["all"]["sites"]))              # this is a LIST in the DICT
#print(my_inventory_yaml["all"]["sites"])                    # this will print list for "sites"
list_all_ip = []                                             # create empty list where IP will be stored
list_all_host = []
#list_all_ip = {}                                               # create empty DICT
for site_dict in my_inventory_yaml["all"]["sites"]:            # this will check dictionary under key "all" and list "sites"
    #print(type(site_dict["hosts"]))    # this is LIST
    #print(type(site_dict))             # this is DICT
    #print(site_dict["hosts"])    # this will print out list under "hosts"
    #print(site_dict)             # this will print out dictionary under "sites"
    for host in site_dict["hosts"]:
    #print(type(host))               # this is DICT
    #print(host)                      # this will print out nested dictionary for every "host"
        for device, device_data in host.items():
            #print(type(device))        # this is STR
            #print(device)              # this print out key values in dictionary
            #print(type(device_data))   # this is nested DICT
            #print(device_data)         # this will print out dictionary for every device
            #print(device_data["ip"])   # this will print out device data for key value "ip", this can be any other key value
            #print(type(device_data["ip"]))                 # this will be STR
            #print(device_data["ip"].split('/')[0])          # this will split str by '/' and print out position0
            ip_list = device_data["ip"].split('/')[0]       # creating valiable to loak cleaner
            list_all_ip.append(ip_list)                   # add every ip from the loop in the list_all_ip list
            list_all_host.append(device)
            #list_all_ip.update(ip_list)
            #print(ip_list)


print(list_all_ip)                                        # this exit the loops and check what is in the new list
print(list_all_host)
#return(list_all_ip)                                        # return can be used if you use function
for x in list_all_host:
    for y in list_all_ip:
        

#for x in list_all_ip:
#    print(x)
login_credentials = my_inventory_yaml["all"]["vars"]
#print(type(login_credentials))
#for x,y in login_credentials.items():
    #print(type(y))
    #print(y)

           
"""                    
    #for address in ip:
    #    print(address + ":" + ip["ip"])
    #for host in site_dict["all"]:
    #for host in site_dict["hosts"]:
        #host_dict = {}
        #print(type(host))
        #   for x in site_dict["hosts"]:
        #        print(x)
                #for y in x:
                    #print(y(0)["ip"])
        #print(host["CORE_01"])
"""