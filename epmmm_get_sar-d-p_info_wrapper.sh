#!/bin/sh

HOSTNAME=$1

DIR=`dirname $0`

CMD="/usr/bin/python3 $DIR/epmmm_get_sar-d-p_info.py -n $HOSTNAME"

$CMD 2>&1 > /dev/null
echo 1