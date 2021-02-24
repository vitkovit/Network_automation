from netmiko import ConnectHandler
from datetime import datetime
import yaml
from pprint import pprint


SH_COMMANDS = ["show running-config"]

with open('inventory_01.yml') as f:
    yaml_content = yaml.safe_load(f)

def show_commands(device, commands):
        start_time = datetime.now()
        hostname = device.pop("name")
        connection = ConnectHandler(**device)
        device_result = ["{0} {1} {0}".format("=" * 15, hostname)]
        print(device_result)
        for command in commands:
            command_result = connection.send_command(command)
            device_result.append("{0} {1} {0}".format("=" * 10, command))
            device_result.append(command_result)

        device_result_string = "\n\n".join(device_result)
        connection.disconnect()
        device_result_string += "\nElapsed time: " + str(datetime.now() - start_time)
        return device_result_string

for device in yaml_content['all']['sites']['hosts']:
    pprint(device)
    connection_data = {
        'device_type': 'cisco_ios',
        'host': yaml_content['all']['sites']['hosts'][device]['ip'],
        'username': yaml_content['all']['vars']['username'],
        'password': yaml_content['all']['vars']['password'],
        'name': yaml_content['all']['sites']['hosts'][device]['name']
    }
    results = show_commands(connection_data, SH_COMMANDS)
    pprint(results)