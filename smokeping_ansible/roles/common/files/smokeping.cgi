# /etc/default/smokeping: Startup configuration for smokeping(1)
#
# select master or slave mode
MODE=master
# in master mode, the rest of the configuration is in
# /etc/smokeping/config
#
# in slave mode, uncomment and set the following variables too
# see smokeping(1)
#
# Mandatory configuration
# MASTER_URL=http://master1.iad.smokeping.symetric.online/cgi-ibin/smokeping.cgi
# SHARED_SECRET=/etc/smokeping/slavesecrets.conf
#
# Optional configuration
# SLAVE_NAME=slave1.smokeping.syd
