zabbix-disk-performance
=======================
Thanks for https://github.com/grundic/zabbix-disk-performance

test pass for python 3.4

test pass for zabbix 2.4

Need:
------
python 3+

pip3 install mysqlclient

pip3 install argparse 

pip3 install py-zabbix

sysstat version:

sysstat-9.0.4-33.el6_9.1.x86_64 

collect info for : iostat -y -x 2 1 
------
Linux 2.6.32-431.el6.x86_64 ()  03/10/2020      _x86_64_        (48 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle

          16.07    0.00    3.70    2.15    0.00   78.08

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util

sdb               0.00     0.00    0.00    2.00     0.00     6.50     3.25     0.01    5.75    0.00    5.75   5.75   1.15


collect info for : sar -d -p 3 1 
------
Linux 2.6.32-431.el6.x86_64 ()  03/10/2020      _x86_64_        (48 CPU)

09:25:30 PM       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util

09:25:33 PM       sdb      7.46      0.00     33.90      4.55      0.05      6.64      5.50      4.10


Average:          DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util

Average:          sdb      7.46      0.00     33.90      4.55      0.05      6.64      5.50      4.10


Zabbix template for collecting IO statistics
------
With this template you can collect different disk statistics.

![Bytes/Sec](https://github.com/grundic/zabbix-disk-performance/blob/master/images/sda_bytes_second.png?raw=true=250x)
![Merged](https://github.com/grundic/zabbix-disk-performance/blob/master/images/sda_merged.png?raw=true=250x)
![Ops/Sec](https://github.com/grundic/zabbix-disk-performance/blob/master/images/sda_ops_second.png?raw=true=250x)
![Overview](https://github.com/grundic/zabbix-disk-performance/blob/master/images/sda_overview.png?raw=true=250x)

Installation
------------
To install, copy `userparameter_diskstats.conf` to `/etc/zabbix/zabbix_agentd.d/userparameter_diskstats.conf` and `lld-disks.py` to `/usr/local/zabbix-agent/scripts/lld-disks.py`.
Do not forget to mark it executable.
```bash
# diskstats user parameters config
sudo mkdir -p /etc/zabbix/zabbix_agentd.d/
sudo wget https://raw.githubusercontent.com/grundic/zabbix-disk-performance/master/userparameter_diskstats.conf -O /etc/zabbix/zabbix_agentd.d/userparameter_diskstats.conf

# low level discovery script
sudo wget https://raw.githubusercontent.com/grundic/zabbix-disk-performance/master/lld-disks.py -O /usr/local/bin/lld-disks.py
sudo chmod +x /usr/local/bin/lld-disks.py
```

`userparameter_diskstats.conf` is user parameters for Zabbix.
`lld-disks.py` is low level discovery script for enumerating disks of your system.

After that restart zabbix-agent
```sudo service zabbix-agent restart```

Go to Zabbix's web interface, Configuration->Templates and import `Template Disk Performance.xml`.
After that you should be able to monitor disk activity for all your disks.

Please note, that items and graphs are created for each disk/partition individually using discovery script, so do not expect to
find them under usual configuration -- they would be in `Discovery rules` section:

![Discovery Rules](https://github.com/grundic/zabbix-disk-performance/blob/master/images/discovery_rules.png?raw=true=250x)

Low level discovery will list your RAID devices, and LVM volumes, but LVM
volumes will be mapped with their device-mapper ID, not the pretty names.

Using without User Parameters
-----------------------------
Zabbix have [standard parameters](https://www.zabbix.com/documentation/2.0/manual/appendix/items/supported_by_platform) for monitoring disk io: `vfs.dev.read` and `vfs.dev.write` with several types:
* sectors
* operations
* sps
* ops

Template have this values configured, but disabled by default.


Testing
-------
To test that everything work use `zabbix_get` (from some time this is in it's own package, so do `apt-get/yum install zabbix-get`):
```bash
# view result of low level discovery
zabbix_get -s 127.0.0.1 -k "custom.vfs.discover_disks"
# view statistics for 'sda' disk
zabbix_get -s 127.0.0.1 -k "custom.vfs.dev.write.sectors[sda]"
# view statistics for iostat or sar info
zabbix_get -s Your Host name's Agent interfaces(IP address) -k "epmmm.get.iostat.info[Your Host name in zabbix,not Visible name.]"
zabbix_get -s 127.0.0.1 -k "epmmm.get.sar-d-p.info[myhost]"
zabbix_get -s 127.0.0.1 -k "epmmm.get.iostat.info[myhost]"

```
