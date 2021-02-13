
from netmiko import ConnectHandler

iou01 = { 
'device_type': 'cisco_ios', 
'ip': '10.0.0.101',
'username': 'cisco', 
'password': 'cisco', 
}

device = ConnectHandler(**iou01)

output1 = device.send_command("show running-config")
save_file = open("iou-core01.txt","w")
save_file.write(output1)
save_file.close()
device.disconnect()
