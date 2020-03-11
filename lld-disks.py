#!/usr/bin/python
import os
import json

if __name__ == "__main__":
    # Iterate over all block devices, but ignore them if they are in the
    # skippable set
    skippable = ("sr", "loop", "ram", "sda1", "sda2", "sda3", "sda4", "sdb1", "sdb2", "sdb3", "sdb4", "sdc1", "sdc2", "sdc3", "sdc4", "sde1", "sdf1", "sdg1", "sdh1")
    devices = (device for device in os.listdir("/sys/class/block")
               if not any(ignore in device for ignore in skippable))
    data = [{"{#DEVICENAME}": device} for device in devices]
    print(json.dumps({"data": data}, indent=4))
