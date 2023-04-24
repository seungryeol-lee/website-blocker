# import tkinter
import time
from datetime import datetime
import yaml

with open("/home/xyzsyz/project/website-blocker/config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


# TODO: Create GUI using tkinter

# TODO: Specify the start time and end time
# TODO: User defined input
# TODO: If stop running, then terminate

# TODO: Add timer function instead of set time
# TODO: When a new list is input: reset the current block and append the new ones only

# From config.yaml
sites_to_block = config["sites"]
system = config["system"]
hostsfile_path = config["hosts_path"][system]
redirect = config["ip_local"]

import sys
import os
import time
import webbrowser
import urllib
from threading import Timer


class Blocker:
    def __init__(self):
        # if sys.platform.startswith("win"):
        #     self.hostsfile_path = "/mnt/c/Windows/System32/drivers/etc/hosts"
        self.hostsfile_path = "/mnt/c/Windows/System32/drivers/etc/hosts"

    def block(self):
        hostsfile = open(self.hostsfile_path, "a+")
        # hostsfile = open(self.hostsfile_path, 'a')
        # Add commentary notes
        #
        hostsfile.write("\n")
        hostsfile.write("# Start of domain blocklist\n")
        for site in sites_to_block:
            hostsfile.write(redirect + "\t\t\t" + site + "\n")
        hostsfile.write("# End of domain blocklist")
        hostsfile.close()

        self.blockTime = int(input())
        t = Timer(self.blockTime, self.unblock)
        t.start()

        print("Domains Blocked!")

    def unblock(self):
        originalFile = []
        ignore = False

        hostsfile_modified = open(self.hostsfile_path, "r+")
        for line in hostsfile_modified:
            if line == "# Start of domain blocklist\n":
                ignore = True
            if ignore == False:
                originalFile.append(line)
            elif line == "# End of domain blocklist":
                ignore = False
        hostsfile_modified.close()

        while originalFile[-1] == "\n":
            originalFile.pop()

        # print(originalFile)

        hostsfile_restored = open(self.hostsfile_path, "w")
        for line in originalFile:
            hostsfile_restored.write(line)
        hostsfile_restored.close()

        print("Domains Unblocked!")


if __name__ == "__main__":
    blocker = Blocker()
    blocker.block()

# TODO: Finish the block / unblock logic
# TODO: Tests
# TODO: CLI execution
# TODO: GUI

"""
def main():
    while True:
        cmd = input("block/unblock: ").lower()
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
"""
