from netmiko import ConnectHandler
import yaml
import datetime
import os

filename = datetime.datetime.now()
TIME=filename.strftime("%d_%m_%Y_%H-%M-%S")

folders=["Config archive", "example"]                       # list of directory you want to create
folder=folders[0]                                           # select witch folder should be created
try:
    os.mkdir(folder)
except FileExistsError:                                     #if file exist python will show "FileExistsError:" error
    print("folder exist: %s" % folder)
else:
    print("Directory created: %s" % folder)

commands = ["show running-config"]

my_inventory = open('inventory_01.yml').read()              # read yaml file .r is not working
my_inventory_yaml = yaml.safe_load(my_inventory)            # readed output saved as variable
for site_dict in my_inventory_yaml["all"]["sites"]:            # this will check dictionary under key "all" and list "sites"
    for host in site_dict["hosts"]:
        host_dict = {}
        host_dict.update({'device_type': 'cisco_ios'})
        host_dict.update(my_inventory_yaml["all"]["vars"])
        for key, value in host.items():
            ip_list = value['ip'].split('/')[0]
            y=dict.fromkeys({'ip'})
            y['ip']=ip_list
            host_dict.update(y)
            for devices in host:
                device_name = devices


                device = ConnectHandler(**host_dict)
                output = device.send_command(commands[0])
                save_file = open("{}/{}_{}.txt".format(folder,device_name,TIME),"w")
                save_file.write(output)
                save_file.close()
                device.disconnect()