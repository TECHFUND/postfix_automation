#!/usr/bin/expect

set timeout 5
spawn alternatives --config mta
expect "Enter"
send "2\n"
interact
