#!/usr/bin/env python3
import getpass
from fabric import Connection, Config

passwd = getpass,getpass("Enter your root password: ")

config = Config(overrides={'sudo': {'password': passwd}})
conn = Connection("127.0.0.1", user="root", config=config)

result = conn.run("ls -la", hide=True) # commands
print(result.stdout)

conn.run("echo 'Hi'")
conn.run("pwd")

with conn.cd("/root/home") # change dir to home dir of root user

conn.sudo("apt install nano") # install nano with root privilges

