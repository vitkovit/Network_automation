import csv
from jinja2 import Template

csv_cource = "config_data.csv"
jinja2_source = "template_interface_types.j2"

with open(jinja2_source) as jinja2file:
    interface_type_template = Template(jinja2file.read(), keep_trailing_newline=True)
#    print(type(interface_type_template))

with open(csv_cource) as csvfile:
    reader = csv.DictReader(csvfile)                               # advantage of header row to create dictionary
    for row in reader:
        interface_config = interface_type_template.render(
            local_intr = row["local-intr"],
            next_device = row["next-device"],
            remote_intr = row["remote-intr"],
            channel_number = row["channel-number"],
            vlan = row["vlan"],
            po_mode = row["po-mode"]
#            device = row["device"]
        )

        print(interface_config)
