from netmiko import ConnectHandler
import yaml
import datetime
import os


#def create_folders(*folder)

#abs_path=os.path.abspath("")
folders=["Config archive", "new"]
#print(abs_path)
#x=os.path.abspath("")
#print(x)
os.mkdir(folder[0]])
except FileExistsError:
    print("Can't create dorectory %s" % path)
else:
    print("Directory created: %s" % path)


folders=["Config archive", "new"]

os.mkdir(folders[0])
except FileExistsError:
    print("Can't create dorectory %s" % path)
else:
    print("Directory created: %s" % path)
