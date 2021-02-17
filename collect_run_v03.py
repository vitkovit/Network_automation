from netmiko import ConnectHandler
import yaml
import datetime
import os

folders=["Config archive", "example"]                       # list of directory you want to create
folder=folders[0]                                           # select witch folder should be created
try:
    os.mkdir(folder)
except FileExistsError:                                     #if file exist python will show "FileExistsError:" error
    print("folder exist: %s" % folder)
else:
    print("Directory created: %s" % folder)

filename = datetime.datetime.now()
TIME=filename.strftime("%d_%m_%Y_%H-%M-%S")

my_inventory = open('inventory_01.yml').read()              # read yaml file .r is not working
my_inventory_yaml = yaml.safe_load(my_inventory)            # readed output saved as variable
for site_dict in my_inventory_yaml["all"]["sites"]:            # this will check dictionary under key "all" and list "sites"
    login_credentials = my_inventory_yaml["all"]["vars"]
    for host in site_dict["hosts"]:
        host_dict = {}
        host_dict.update({'device_type': 'cisco_ios'})
        host_dict.update(login_credentials)
        for key, value in host.items():
            ip_list = value['ip'].split('/')[0]
            y=dict.fromkeys({'ip'})
            y['ip']=ip_list
            host_dict.update(y)
            for key in host:
                q=[]
                q.append(key)
                name=key
                x=dict.fromkeys(q,host_dict)            
                device = ConnectHandler(**host_dict)
                output = device.send_command("show running-config")
                save_file = open("{}/{}_{}.txt".format(folder,name,TIME),"w")
                save_file.write(output)
                save_file.close()
                device.disconnect()