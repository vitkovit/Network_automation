
from netmiko import ConnectHandler
import yaml
import datetime
  
# datetime.datetime.now() to get  
# current date as filename. 
filename = datetime.datetime.now()
x=filename.strftime("%d_%m_%Y_%H:%M:%S")
print(x)
"""
iou01 = { 
'device_type': 'cisco_ios', 
'ip': '10.0.0.101',
'username': 'cisco', 
'password': 'cisco', 
}
print(type(iou01))

device = ConnectHandler(**iou01)

output1 = device.send_command("show running-config")
save_file = open("iou-core01.txt","w")
save_file.write(output1)
save_file.close()
device.disconnect()"""

