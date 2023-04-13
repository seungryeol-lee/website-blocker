# import tkinter
import time
from datetime import datetime

# TODO: Create GUI using tkinter
# time.sleep(1)

# TODO: Specify the start time and end time
end_time = datetime(2023, 4, 12, 14)

# TODO: Create a separate text document for store all the websites to block
# TODO: When a new list is input: reset the current block and append the new ones only
sites_to_block = []

# TODO: Create separate variables for two hosts
# hosts_path = "/etc/hosts"
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_path = "/mnt/c/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

# TODO: Improve the algorithm and logic
# TODO: Create a class object
def block_sites():
    if datetime.now() < end_time:
        print("block sites")
        with open(hosts_path, "r+") as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:
        print("unblock sites")
        with open(hosts_path, "r+") as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostsfile.truncate()


if __name__ == "__main__":
    block_sites()
