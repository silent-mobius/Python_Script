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
