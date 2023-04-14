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

# TODO: Add timer function instead of set time
# TODO: When a new list is input: reset the current block and append the new ones only

# From config.yaml
sites_to_block = config["sites"]
system = config["system"]
hosts_path = config["hosts_path"][system]
redirect = config["ip_local"]


# TODO: Rethink about the process


# TODO: Improve the algorithm and logic
# TODO: Create a class object
def main():
    while True:
        cmd = input("Block/Unblock: ").lower()
        if cmd == "block":
            date_entry = input("YYYY-MM-DD-HH: ")
            year, month, day, hour = map(int, date_entry.split("-"))
            end_time = datetime(year, month, day, hour)
            block_sites(end_time)
            break
        elif cmd == "unblock":
            unblock_sites()
            break
        else:
            print("Invalid input")
            continue


def block_sites(end_time):
    if datetime.now() < end_time:
        print("Blocking sites")
        with open(hosts_path, "r+") as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")


def unblock_sites():
    print("Unblocking sites")
    with open(hosts_path, "r+") as hostsfile:
        lines = hostsfile.readlines()
        hostsfile.seek(0)
        for line in lines:
            if not any(site in line for site in sites_to_block):
                hostsfile.write(line)
        hostsfile.truncate()


if __name__ == "__main__":
    main()
