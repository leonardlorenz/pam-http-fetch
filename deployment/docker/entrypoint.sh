#!/bin/sh

ip addr | grep inet | grep brd | sed 's/  //g'

echo "root:$(cat /rootpw.txt)" | chpasswd

echo "root password: $(cat /rootpw.txt)"

/usr/sbin/sshd -p 22 -D
