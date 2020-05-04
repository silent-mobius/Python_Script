#!/usr/bin/env python3

# Import the module
import subprocess

# Ask the user for input
host = input("Enter a host to ping: ")	

# Set up the echo command and direct the output to a pipe
p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)

# Run the command
output = p1.communicate()[0]

print(output)


target = input("Enter an IP or Host to ping: ")

host = subprocess.Popen(['host', target], stdout = subprocess.PIPE).communicate()[0]

print(host)


subprocess.call(["ls", "-lha"])

cp = subprocess.run(["ls -lha"],shell=True)

cp

cp = subprocess.run(["ls","-lha"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

cp.stdout

cp.stderr
# '' (empty string)
cp.returncode
# 0


cp = subprocess.run(["ls","foo bar"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

cp.output
# '' (empty string)
cp.stderr
# ls: cannot access 'foo bar': No such file or directory
cp.returncode
# 2


### pipe the output - just like in bash 
from subprocess import Popen,PIPE

# this is equivalent to ls -lha | grep "foo bar"
p1 = Popen(["ls","-lha"], stdout=PIPE)
p2 = Popen(["grep", "foo bar"], stdin=p1.stdout, stdout=PIPE)
p1.stdout.close()

output = p2.communicate()[0]
 
