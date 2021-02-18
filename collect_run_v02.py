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
import datetime
from pprint import pprint
  

filename = datetime.datetime.now()
TIME=filename.strftime("%d_%m_%Y_%H-%M-%S")


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
#list_all_ip = []                                             # create empty list where IP will be stored
#list_all_host = []
#list_all_ip = {}                                               # create empty DICT
#host_dict = {}
for site_dict in my_inventory_yaml["all"]["sites"]:            # this will check dictionary under key "all" and list "sites"
    #print(my_inventory_yaml["all"]["sites"]["hosts"])
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
#            ip_list = device_data["ip"].split('/')[0]       # creating valiable to loak cleaner
#            list_all_ip.append(ip_list)                   # add every ip from the loop in the list_all_ip list
#            list_all_host.append(device)
            #list_all_ip.update(ip_list)
            #print(ip_list)
            
    login_credentials = my_inventory_yaml["all"]["vars"]
    #print(site_dict["hosts"])
    #print(type(site_dict["hosts"]))
    for host in site_dict["hosts"]:
        #print(type(host))
        host_dict = {}
        host_dict.update({'device_type': 'cisco_ios'})
        host_dict.update(host)
        host_dict.update(login_credentials)
        #print(host_dict)
        #print(host_dict['username'])
        name=str(host)
        #print(name)
        #print(host)
        
        #for w in host["interfaces"]:
            #print(w)
        for key, value in host.items():
            #print(type(value["interfaces"]["lo0"]))
            ip_list = value['ip'].split('/')[0]
            y=dict.fromkeys({'ip'})
            y['ip']=ip_list
            host_dict.update(y)
            print(host_dict)
            #for value2 in value["interfaces"]:
            #    print(value)
                for key in host:
                q=[]
                q.append(key)
                name=key
                print(name)

        #        device = ConnectHandler(**value)
        #        output = device.send_command("show running-config")
        #        save_file = open("{}_{}.txt".format(name,TIME),"w")
        #        save_file.write(output)
        #       ave_file.close()
        #        device.disconnect()
        #        print(device)

            #for key2, value2 in key.items():
            #    print(value2)
            #print(type(key))
            #ip_list= []
            #print(type(value))
            #for w in value:
            #    print(w)
            #print(host)
            #for
            #for
            #y=[]
            #y.append(value)
            #ip_list.append(value['ip'].split('/')[0])
            #ip_list = value['ip'].split('/')[0]
            #print(host_dict)                        # this will print dictionary device type, username, password
            #x=ip_list
            #return ip_list
            #print(type(x))                                 # this will print list on IP addresses
            #print(ip_list)
            #y=dict.fromkeys({'ip'})
            #y['ip']=ip_list
            
            #print(y)
            #    print(q)
        #    host_dict.update(y)
            #site_dict.update(host_dict)
            #print(host_dict)                           # final format - need to be assigned to new key
            #print(type(host_dict))
            
            #print(site_dict)
            #z = {}
            #for key in host.keys():
            #    key=dict(key + host_dict)
            #    print(key)
        #    for key in host:
        #        q=[]
        #        q.append(key)
                #print(type(q))
        #        name=key
        #        print(q)
                #print(name)
        #        x=dict.fromkeys(q,host_dict)
        #        print((x)
                #print(type(x))
                #print(len(x))
                

        #        device = ConnectHandler(**value)
        #        output = device.send_command("show running-config")
        #        save_file = open("{}_{}.txt".format(name,TIME),"w")
        #        save_file.write(output)
        #       ave_file.close()
        #        device.disconnect()
        #        print(device)
            

            #print(ip_list)
            #for y in host_dict:
            #    y=dict.fromkeys()
            #    host_dict.update(y)
            #print(host_dict)
            #host_dict.update(x)
            #print(ip_list)
            #host_dict[key].append(ip_list)
            #x=value['ip'].split('/')[0]
            #host_dict.update({'ip':value})
            #host_dict.update(value['ip'],'a')
            #host_dict.update(x)
           # print(ip_list)
            #print(host_dict)
#print(host_dict)           
# 'device_type': 'cisco_ios', 
#'ip': '10.0.0.101',
#'username': 'cisco', 
#'password': 'cisco',      




#x=zip(list_all_host, list_all_ip)                                        # this exit the loops and check what is in the new list
#print(list_all_ip)
#x = dict(zip(list_all_host,list_all_ip))
#print(x)
#x=dict.fromkeys(list_all_host, list_all_ip)
#print(x)
#return(list_all_ip)                                        # return can be used if you use function
#for x in list_all_host:
 #   for y in list_all_ip:


#for x in list_all_ip:
#    print(x)
#login_credentials = my_inventory_yaml["all"]["vars"]
#print(type(login_credentials))
#for x,y in login_credentials.items():
    #print(type(y))
    #print(y)