import csv
from jinja2 import Template
import pandas as pd
import numpy as np

csv_source = "config_data.csv"
jinja2_source = "template_interface_types.j2"

with open(jinja2_source) as jinja2file:
# keep_trailing_newline=True is used to add empty line between each configuration
    interface_type_template = Template(jinja2file.read(), keep_trailing_newline=True)

# read file reader with panda, but read as csv
fill_reader = pd.read_csv("config_data.csv")                               
# convert "vlan" column to integer type with numpy, if not, vlan will be 999.0 (float)
fill_reader["vlan"] = np.nan_to_num(fill_reader["vlan"]).astype(int)
# read "device" column and fill empty spaces with value of first field
fill_reader["device"] = fill_reader["device"].fillna(method='ffill')
# every empty field will habe NaN in it, so replace this with "" (empty) value
fill_reader = fill_reader.replace(np.nan, "")

# convert fill_reader to dictionary ‘records’ will list in form [{column -> value}, ...]
converted_data_csv = fill_reader.to_dict(orient='records')
interface_configs = ""
for row in converted_data_csv:
#for every row in csv file render it with jinja2 template
    interface_config = interface_type_template.render(
        local_intr = row["local-intr"],
        next_device = row["next-device"],
        remote_intr = row["remote-intr"],
        channel_number = row["channel-number"],
        vlan = row["vlan"],
        po_mode = row["po-mode"],
        #just for funn add comment to know on witch device configuration is happening
        device_name = row["device"]
    )
    interface_configs += interface_config
#TBC.... need to make condition for connecting to the device
    if row["device"] == "CORE_01":
        print(interface_config)
#    print(row)
    #with open("interface_configs.txt", "w") as f:
    #    f.write(interface_configs)
 #   config_set = interface_configs.split("\n") # this will split to every new line as a list
 #   print(config_set)