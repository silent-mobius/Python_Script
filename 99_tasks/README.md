Write a Python script that sets the following variables:

    first_name - Set to your first name
    last_name - Set to your last name
    age - Set to your age as an integer
    birth_date - Set to your birthdate as a string

Using the variables, print the following to the screen when you run the script:

My name is FIRST_NAME LAST_NAME.
I was born on BIRTH_DATE and I'm AGE years old.

---

Create a script that has a single variable you can set at the top called user. This user is a dictionary containing the keys:

    'admin' - a boolean representing whether the user is an admin user.
    'active' - a boolean representing whether the user is currently active.
    'name' - a string that is the user’s name.

Example:

user = { 'admin': True, 'active': True, 'name': 'Kevin' }

Depending on the values of user, print one of the following to the screen when you run the script:

    print (ADMIN) followed by the user’s name if the user is an admin.
    print ACTIVE - followed by the user’s name if the user is active.
    print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin and active.
    print the user’s name if neither active nor an admin.

Change the values of user and re-run the script multiple times to ensure that it works.

---

Building on top of the conditional exercise, write a script that will loop through a list of users, where each item is a user dictionary from the previous exercise, printing out each user’s status on a separate line. Additionally, print the line number at the beginning of each line, starting with line 1. Be sure to include a variety of user configurations in the users list.

User Keys:

    'admin' - a boolean representing whether the user is an admin user.
    'active' - a boolean representing whether the user is currently active.
    'name' - a string that is the user’s name.

Depending on the values of the user, print one of the following to the screen when you run the script:

    print (ADMIN) followed by the user’s name if the user is an admin.
    print ACTIVE - followed by the user’s name if the user is active.
    print ACTIVE - (ADMIN) followed by the user’s name if the user is an admin and active.
    print the user’s name if neither active nor an admin.

---

Which of these values would cause an if block to execute if used as the if statement's conditional?

(Possible Correct: 2)

[1, 2]

1 > 2

"test"

0

---
What keyword is used for a second "if" in an if/else chain?

elsif

elseif

else if

elif

---

What does REPL stand for?

Read Evaluate Print Loop

Real-Time Evaluated Python Logic

None of these answers.

Read Expression Per Line

---

What value represents nothingness in Python?

0

None

nil

null

---

Which of the following shebangs can you leverage to use the system Python on a CentOS system?

#!/sbin/python

#!/usr/local/bin/python

#!/bin/python

#!~/bin/python

---

How can you run a non-executable Python file?

python exec file.py

python run file.py

None of the answers listed are correct.

python file.py

---

Which of these are valid strings?

(Possible Correct: 2)

"Hello 'Doug'"

'How's the weather outside?'

"It's time to\nrock"

"My name's "Doug""
---

What would the result of 4 * '1.1' be?

'1.11.11.11.1'

4.4

'4.4'

TypeError

---

Which of these would have a float for the result?

(Possible Correct: 2)

2 * 1

float(6 * 3)

3 * str(2.0)

2.0 / 3

---

Which of these "is" comparisons will return True?

(Possible Correct: 2)

'a' is 'a'

1 is True

1 is 1

[1] is [1]

---

What type of loop is used to create an infinite loop? (Choose the option with the most straightforward implementation.)

A do ... while loop.

A while loop.

A for loop.

You cannot create an infinite loop in Python.

---

How would you create a new variable with the value "test"?

let foo = "test"

foo = "test"

var foo string = "test"

foo == "test"

---

How would you get the value of the key 'color' from a dictionary called 'favorites'?

favorites[color]

None of the answers listed

favorites['color']

favorites.read('color')

---

Which of these can be used as a key in a dictionary?

(Possible Correct: 3)

'Kevin'

1

(1, 2)

[1, 2, 3]

---

Functions are a great way to organize your code for reuse and clarity. Write a script that does the following:

    Prompts the user for a message to echo
    Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
    Defines a function that takes a message and count, then prints the message that many times.

To end the script, call the function with the user-defined values to print to the screen.

---

Functions are a great way to organize your code for reuse and clarity. Write a script that does the following:

    Prompts the user for a message to echo
    Prompts the user for the number of times to repeat the message. If no response is given, then the count should default to 1.
    Defines a function that takes a message and count, then prints the message that many times.

To end the script, call the function with the user-defined values to print to the screen.

---

Environment variables are often used for configuring command line tools and scripts. Write a script that does the following:

    Prints the first ten digits of Pi to the screen.
    Accepts an optional environment variable called DIGITS. If present, the script will print that many digits of Pi instead of 10.

Note: You’ll want to import pi from the math package.

This task will require some more advanced string formatting. You can read the documentation here, but here’s an example of how you could print a float to ten digits:

print("%.*f" % (10, my_float))

---

Write a script that prompts the user for:

    A file_name where it should write the content.
    The content that should go in the file. The script should keep accepting lines of text until the user enters an empty line.

After the user enters an empty line, write all of the lines to the file and end the script.

---

Write a script that does the following:

    Receives a file_name and line_number as command line parameters.
    Prints the specified line_number from file_name to the screen. The user will specify this as you would expect, not using zero as the first line.

Make sure that you handle the following error cases by presenting the user with a useful message:

    The file doesn’t exist.
    The file doesn’t contain the line_number specified (file is too short).

---
It’s not uncommon for a process to run on a server and listen to a port. Unfortunately, you sometimes don’t want that process to keep running, but all you know is the port that you want to free up. You’re going to write a script to make it easy to get rid of those pesky processes.

Write a script that does the following:

    Takes a port_number as its only argument.
    Calls out to lsof to determine if there is a process listening on that port.
        If there is a process, kill the process and inform the user.
        If there is no process, print that there was no process running on that port.

Python's standard library comes with an HTTP server that you can use to start a server listening on a port (5500 in this case) with this line:

$ python -m SimpleHTTPServer 5500

Use a separate terminal window/tab to test our your script to kill that process.

Hints:

    You may need to install lsof. Use this command:

    $ sudo yum install -y lsof

    Use this line of lsof to get the port information:

    lsof -n -i4TCP:PORT_NUMBER

    That will return multiple lines, and line you’ll want will contain “LISTEN”.
    Use the string split() method to break a string into a list of its words.

    You can either use the kill command outside of Python or the os.kill(pid, 9) function.

---

You’ve now written a few scripts that handle errors, but when the failures happen the status code returned is still a success (0).

Improve your script to kill processes by exiting with an error status code when there isn’t a process to kill

---

Which of these types can be iterated over?

(Possible Correct: 3)

list

string

float

dictionary

---

Which of these values would cause an if block to execute if used as the if statement's conditional?

(Possible Correct: 2)

[1, 2]

1 > 2

"test"

0

---

When can you use a comment in Python?

(Possible Correct: 3)

After the final expression on a line.

At the beginning of a line.

In the middle of a function's parentheses.

At the beginning of a file.

---

Which of these for loop declarations is NOT valid?

(Possible Correct: 2)

for i = 0; i < 10; i++:

for x in [1, 2, 3]:

for x, y in [(1, 2), (2, 3), (3,4)]:

for x, y in [1, 2, 3]:

---

What is the file extension for Python?

.p

.python

.py

.egg

---

How would you create a new variable with the value "test"?

let foo = "test"

foo = "test"

var foo string = "test"

foo == "test"

---

Which tuples could be used in print("%s %s" % my_tuple) without causing an error?

(Possible Correct: 2)

('a',)

('a', 'b')

(2.0, 3.0)

(1, 2, 3)

---

How would you get every item with an even index (0, 2, 4, etc.) from a list using slicing?

my_list[:2]

my_list[::2]

None of the answers listed.

my_list[2:]

---

Utilize pip to install the psycopg2 library (a PostgreSQL database library). Be sure to first create and activate a virtualenv before installing the package

---

Make sure that you have the requests package installed. Now, write a script that does the following:

    Accepts a URL and destination file name from the user calling the script.
    Utilizes requests to make an HTTP request to the given URL.
    Has an optional flag to state whether or not the response should be JSON or HTML (HTML by default).
    Writes the contents of the page out to the destination.

Note: You’ll want to use the text attribute to get the HTML. To write this content on Python 2, you’ll need to convert the unicode object to a string by using res.text.encode("UTF-8").

---

What command would you use to upgrade an installed Python package? Example: boto3

pip boto3

pip install --upgrade boto3

pip update boto3

pip upgrade boto3

---

When using pip, what is the standardized name for a file listing dependencies?

None of the answers listed

EGG file

Wheel file

requirements.txt

---

Over the course of the next few exercises, you’ll be creating a Python package to manage users on a server based on an “inventory” JSON file. The first step in this process is going to be setting up the project’s directory structure and metadata.

Do the following:

    Create a project folder called hr (short for “human resources”)
    Set up the directories to put the project’s source code and tests.
    Create the setup.py with metadata and package discovery.
    Utilize pipenv to create a virtualenv and Pipfile.
    Add pytest and pytest-mock as development dependencies.
    Set the project up in source control and make your initial commit.

---

The ideal usage of the hr command is this:

$ hr path/to/inventory.json
Adding user 'kevin'
Updating user 'lisa'
Removing user 'alex'

The alternative usage of the CLI will be to pass a --export flag like so:

$ hr --export path/to/inventory.json

This --export flag won’t take any arguments. Instead, you’ll want to default the value of this field to False and set the value to True if the flag is present. Look at the action documentation to determine how you should go about doing this.

For this exercise, Write a few tests before implementing a CLI parser. Ensure the following:

    An error is raised if no arguments are passed to the parser.
    No error is raised if a path is given as an argument.
    The export value is set to True if the --export flag is given.

---

The tool you’re building is going to be running on Linux systems and it’s safe to assume that it’s going to run via sudo. With this information it’s safe to say that the tool can utilize usermod, useradd, and userdel to keep users on the server up to date.

Create a module in your package to work with user information. You’ll want to be able to do the following:

    Received a list of user dictionaries and ensure that the system’s users match.
    Have a function that can create a user with the given information if no user exists by that name.
    Have a function that can update a user based on a user dictionary.
    Have a function that can remove a user with a given username.
    The create, update, and remove functions should print that they are creating/updating/removing the user before executing the command.

The user information will come in the form of a dictionary shaped like this:

{
  'name': 'kevin',
  'groups': ['wheel', 'dev'],
  'password': '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'
}

The password values will be SHA512 encrypted.

Hint: You can generate an encrypted password in Python that is usable with usermod -p with this snippet:

import crypt

crypt.crypt('password', crypt.mksalt(crypt.METHOD_SHA512))

Tools to Consider:

You’ll likely want to interface with the following unix utilities:

    useradd
    usermod
    userdel

Python modules you’ll want to research:

    pwd - Password/User database.
    grp - Group database.

Be careful in testing not to delete your own user or change your password to something that you don’t know.

---

The last module that you’ll implement for this package is one for interacting with the user inventory file. The inventory file is a JSON file that holds user information. The module needs to:

    Have a function to read a given inventory file, parse the JSON, and return a list of user dictionaries.
    Have a function that takes a path, and produces an inventory file based on the current state of the system. An optional parameter could be the specific users to export.

Python modules you’ll want to research:

    json - Interact with JSON from Python.
    grp - Group database.
    pwd - Password/user database.
    spwd - Shadow Password database. (Used to get current encrypted password)

Example inventory JSON file:

[
  {
    "name": "kevin",
    "groups": ["wheel", "dev"],
    "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
  },
  {
    "name": "lisa",
    "groups": ["wheel"],
    "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
  },
  {
    "name": "jim",
    "groups": [],
    "password": "$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/"
  }
]

Hint: If you’re writing tests for this code you’ll need to heavily rely on mocking to make the interactions with modules like grp, pwd, and spwd consistent.

---

    Implement main function that ties all of the modules together based on input to the CLI parser.
    Modify the setup.py so that when installed there is an hr console script.

---

Now that you know the tools works it’s time to build it for distribution. Build a wheel for the package and use it to install the hr tool on your system.

Note: This package doesn’t support Python 3, so it is not a “universal” package.

---

How do you create a package in a Python project?

Name a Python file with the package name you want to create.

Prefix the file name with package_.

None of the answers listed are correct.

Put an __init__.py file in a directory with the desired name.

---

What single tool can you use to create virtualenvs and manage dependencies?

pipenv

pip

venv

virtualenv

---

how do you access a file in Python?

File('filename.txt')

open('filename.txt')

os.readfile('filename.txt')

None of the answers listed

---

Which keywords are part of the error catching functionality in Python?

(Possible Correct: 3)

catch

try

else

except

---

Which of these function calls is valid for this function definition: def area(length, width, height=1):?

(Possible Correct: 2)

area(width=2, height=2, length=2)

area(length=2, 2, 2)

area(2, width=2)

area(1, 2)

---

How would you access the "path" attribute on a Namespace object called "args"?

None of the answers listed.

args.path()

args.path

args['path']

---

Which of the following are valid ways to load in additional Python libraries?

(Possible Correct: 2)

import time

from time import strftime, localtime

require time

import strftime, localtime from time
