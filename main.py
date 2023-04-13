# import tkinter
import time
from datetime import datetime
import yaml

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


# TODO: Create GUI using tkinter
# time.sleep(1)

# TODO: Specify the start time and end time
# TODO: User defined input
# TODO: If stop running, then terminate
end_time = datetime(2023, 4, 12, 14)

# TODO: When a new list is input: reset the current block and append the new ones only

# From config.yaml
sites_to_block = config["sites"]
system = config["system"]
hosts_path = config["hosts_path"][system]
redirect = config["ip_local"]


# TODO: Improve the algorithm and logic
# TODO: Create a class object
def block_sites():
    if datetime.now() < end_time:
        print("Blocking sites")
        with open(hosts_path, "r+") as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:
        print("Unblocking sites")
        with open(hosts_path, "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostsfile.truncate()


if __name__ == "__main__":
    block_sites()
