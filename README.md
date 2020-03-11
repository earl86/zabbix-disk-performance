zabbix-disk-performance
=======================
test pass for python 3.4

pip3 install argparse 
pip3 install py-zabbix

test pass for zabbix 2.4

sysstat version:sysstat-9.0.4-33.el6_9.1.x86_64 
collect info for : iostat -y -x 2 1 
Linux 2.6.32-431.el6.x86_64 ()  03/10/2020      _x86_64_        (48 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          16.07    0.00    3.70    2.15    0.00   78.08

Device:         rrqm/s   wrqm/s     r/s     w/s   rsec/s   wsec/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
sdb               0.00     0.00    0.00    2.00     0.00     6.50     3.25     0.01    5.75    0.00    5.75   5.75   1.15
sda               0.00     0.00    0.00    2.00     0.00     6.50     3.25     0.01    3.75    0.00    3.75   3.75   0.75
sdq               0.00     0.00    0.00   95.50     0.00 30880.00   323.35     0.19    1.96    0.00    1.96   1.88  17.95
sdo               0.00     0.00    0.00  104.00     0.00 31072.00   298.77     0.19    1.82    0.00    1.82   1.78  18.55
sdm               0.00     0.00    0.00  102.00     0.00 31056.00   304.47     0.18    1.76    0.00    1.76   1.65  16.85
sdp               0.00     0.00    0.00   95.50     0.00 30880.00   323.35     0.17    1.76    0.00    1.76   1.73  16.50
sdn               0.00     0.00    0.00  104.00     0.00 31072.00   298.77     0.16    1.54    0.00    1.54   1.52  15.80
sdw               0.00     0.00    0.00   96.00     0.00 30708.00   319.88     0.17    1.77    0.00    1.77   1.62  15.55
sdr               0.00     0.00    0.00  168.00     0.00 31516.00   187.60     0.36    2.14    0.00    2.14   1.95  32.70
sdl               0.00     0.00    0.00  102.00     0.00 31056.00   304.47     0.17    1.62    0.00    1.62   1.50  15.25
sds               0.00     0.00    0.00  168.00     0.00 31516.00   187.60     0.34    2.04    0.00    2.04   1.83  30.70
sdt               0.00     0.00    0.00  168.50     0.00 31516.00   187.04     0.33    1.93    0.00    1.93   1.69  28.50
sdv               0.00     0.00    0.00   96.50     0.00 30716.00   318.30     0.20    2.05    0.00    2.05   1.90  18.30
sdu               0.00     0.00    0.00  168.00     0.00 31260.00   186.07     0.32    1.88    0.00    1.88   1.68  28.15
sdg               0.00     0.00  143.50  326.00  1944.00  5628.00    16.13     0.05    0.10    0.13    0.09   0.09   4.10
sdy               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
sdc               0.00     0.00  124.00  283.50  1708.00  7008.00    21.39     0.06    0.15    0.18    0.14   0.12   4.85
sdx               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
sdh               0.00     0.00    2.50  326.00    36.00  5628.00    17.24     0.03    0.09    0.20    0.09   0.07   2.35
sdd               0.00     0.00    5.00  283.50    68.00  7008.00    24.53     0.03    0.10    0.20    0.10   0.08   2.40
sdf               0.00     0.00    4.50  343.50    60.00  6504.00    18.86     0.04    0.11    0.11    0.11   0.08   2.75
sde               0.00     0.00  140.50  343.50  1840.00  6504.00    17.24     0.06    0.12    0.14    0.12   0.09   4.50
sdk               0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
sdj               0.00     0.00    3.50  328.50    48.00  5652.00    17.17     0.04    0.12    0.14    0.12   0.09   2.85
sdi               0.00     1.50  144.00  327.00  1904.00  5652.00    16.04     0.06    0.12    0.12    0.12   0.10   4.70
md0               0.00     0.00    0.00    0.50     0.00     4.00     8.00     0.00    0.00    0.00    0.00   0.00   0.00
md2               0.00     0.00    0.00  734.00     0.00 186740.00   254.41     0.00    0.00    0.00    0.00   0.00   0.00
md1               0.00     0.00  567.50 1281.50  7608.00 24792.00    17.52     0.00    0.00    0.00    0.00   0.00   0.00

collect info for : sar -d -p 3 1 

Linux 2.6.32-431.el6.x86_64 ()  03/10/2020      _x86_64_        (48 CPU)

09:25:30 PM       DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
09:25:33 PM       sdb      7.46      0.00     33.90      4.55      0.05      6.64      5.50      4.10
09:25:33 PM       sda      7.46      0.00     33.90      4.55      0.05      6.64      6.09      4.54
09:25:33 PM       sdq    102.71      0.00  32149.15    313.00      0.18      1.76      1.64     16.88
09:25:33 PM       sdo    115.59      0.00  32461.02    280.82      0.22      1.90      1.84     21.25
09:25:33 PM       sdm    142.37      0.00  32813.56    230.48      0.28      1.98      1.90     27.05
09:25:33 PM       sdp    103.05      0.00  32151.86    312.00      0.20      1.96      1.81     18.64
09:25:33 PM       sdn    115.25      0.00  32287.46    280.14      0.27      2.35      2.24     25.86
09:25:33 PM       sdw    190.85      0.00  33475.25    175.40      0.31      1.63      1.44     27.49
09:25:33 PM       sdr     99.32      0.00  32230.51    324.51      0.15      1.53      1.42     14.10
09:25:33 PM       sdl    142.37      0.00  32813.56    230.48      0.31      2.15      1.97     28.07
09:25:33 PM       sds     99.32      0.00  32230.51    324.51      0.16      1.60      1.43     14.17
09:25:33 PM       sdt    121.02      0.00  32642.71    269.74      0.20      1.63      1.44     17.39
09:25:33 PM       sdv    190.85      0.00  33475.25    175.40      0.33      1.70      1.53     29.22
09:25:33 PM       sdu    121.02      0.00  32642.71    269.74      0.19      1.58      1.46     17.66
09:25:33 PM       sdg    638.31   3487.46   8951.86     19.49      0.08      0.13      0.11      6.95
09:25:33 PM       sdy      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
09:25:33 PM       sdc    651.19   3254.24  10603.39     21.28      0.09      0.14      0.12      7.49
09:25:33 PM       sdx      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
09:25:33 PM       sdh    418.64    273.90   8951.86     22.04      0.04      0.10      0.07      3.12
09:25:33 PM       sdd    433.56    162.71  10603.39     24.83      0.05      0.13      0.10      4.41
09:25:33 PM       sdf    435.93    265.76   8778.31     20.75      0.04      0.10      0.09      3.73
09:25:33 PM       sde    663.39   3520.00   8778.31     18.54      0.08      0.12      0.11      7.19
09:25:33 PM       sdk      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
09:25:33 PM       sdj    389.49    168.14   8607.46     22.53      0.03      0.09      0.08      2.98
09:25:33 PM       sdi    616.95   3473.90   8607.46     19.58      0.07      0.11      0.09      5.69
09:25:33 PM       md0      3.39      0.00     27.12      8.00      0.00      0.00      0.00      0.00
09:25:33 PM       md2    771.86      0.00 195772.20    253.64      0.00      0.00      0.00      0.00
09:25:33 PM       md1   2629.15  14603.39  36941.02     19.60      0.00      0.00      0.00      0.00

Average:          DEV       tps  rd_sec/s  wr_sec/s  avgrq-sz  avgqu-sz     await     svctm     %util
Average:          sdb      7.46      0.00     33.90      4.55      0.05      6.64      5.50      4.10
Average:          sda      7.46      0.00     33.90      4.55      0.05      6.64      6.09      4.54
Average:          sdq    102.71      0.00  32149.15    313.00      0.18      1.76      1.64     16.88
Average:          sdo    115.59      0.00  32461.02    280.82      0.22      1.90      1.84     21.25
Average:          sdm    142.37      0.00  32813.56    230.48      0.28      1.98      1.90     27.05
Average:          sdp    103.05      0.00  32151.86    312.00      0.20      1.96      1.81     18.64
Average:          sdn    115.25      0.00  32287.46    280.14      0.27      2.35      2.24     25.86
Average:          sdw    190.85      0.00  33475.25    175.40      0.31      1.63      1.44     27.49
Average:          sdr     99.32      0.00  32230.51    324.51      0.15      1.53      1.42     14.10
Average:          sdl    142.37      0.00  32813.56    230.48      0.31      2.15      1.97     28.07
Average:          sds     99.32      0.00  32230.51    324.51      0.16      1.60      1.43     14.17
Average:          sdt    121.02      0.00  32642.71    269.74      0.20      1.63      1.44     17.39
Average:          sdv    190.85      0.00  33475.25    175.40      0.33      1.70      1.53     29.22
Average:          sdu    121.02      0.00  32642.71    269.74      0.19      1.58      1.46     17.66
Average:          sdg    638.31   3487.46   8951.86     19.49      0.08      0.13      0.11      6.95
Average:          sdy      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
Average:          sdc    651.19   3254.24  10603.39     21.28      0.09      0.14      0.12      7.49
Average:          sdx      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
Average:          sdh    418.64    273.90   8951.86     22.04      0.04      0.10      0.07      3.12
Average:          sdd    433.56    162.71  10603.39     24.83      0.05      0.13      0.10      4.41
Average:          sdf    435.93    265.76   8778.31     20.75      0.04      0.10      0.09      3.73
Average:          sde    663.39   3520.00   8778.31     18.54      0.08      0.12      0.11      7.19
Average:          sdk      0.00      0.00      0.00      0.00      0.00      0.00      0.00      0.00
Average:          sdj    389.49    168.14   8607.46     22.53      0.03      0.09      0.08      2.98
Average:          sdi    616.95   3473.90   8607.46     19.58      0.07      0.11      0.09      5.69
Average:          md0      3.39      0.00     27.12      8.00      0.00      0.00      0.00      0.00
Average:          md2    771.86      0.00 195772.20    253.64      0.00      0.00      0.00      0.00
Average:          md1   2629.15  14603.39  36941.02     19.60      0.00      0.00      0.00      0.00


Zabbix template for collecting IO statistics

With this template you can collect different disk statistics.

![Bytes/Sec](https://github.com/grundic/zabbix-disk-performance/blob/master/images/sda_bytes_second.png?raw=true=250x)
![Merged](https://github.com/grundic/zabbix-disk-performance/blob/master/images/sda_merged.png?raw=true=250x)
![Ops/Sec](https://github.com/grundic/zabbix-disk-performance/blob/master/images/sda_ops_second.png?raw=true=250x)
![Overview](https://github.com/grundic/zabbix-disk-performance/blob/master/images/sda_overview.png?raw=true=250x)

Installation
------------
To install, copy `userparameter_diskstats.conf` to `/etc/zabbix/zabbix_agentd.d/userparameter_diskstats.conf` and `lld-disks.py` to `/usr/local/bin/lld-disks.py`.
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
```
