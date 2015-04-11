#!/usr/bin/expect

set timeout 5
spawn passwd info
expect "New password:"
send "Tx2W7rBR\n"
expect "Retype new password:"
send "Tx2W7rBR\n"
interact
