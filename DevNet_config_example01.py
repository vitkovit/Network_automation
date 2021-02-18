from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type = 'cisco_ios',
    host = '192.168.1.1',
    port = 22,
    username = 'cisco',
    password = 'cisco123!'
    )

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))

config_commands = [
    'int loopback 1',
    'ip add 10.1.1.1 255.255.255.0',
    'description [Student Name]\'s loopback'
    ]

sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))

config_commands = [
    'int loopback 2',
    'ip add 10.1.1.1 255.255.255.0',
    'description [Student Name]\'s loopback'
    ]

sentConfig = sshCli.send_config_set(config_commands)
print("{}\n".format(sentConfig))

output = sshCli.send_command("sh ip int br")
print("{}\n".format(output))