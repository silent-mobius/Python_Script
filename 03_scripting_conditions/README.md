# Python Script Flow Control

## Python Conditions and If statements

Python supports the usual logical conditions from mathematics:

*  Equals: a == b
*  Not Equals: a != b
*  Less than: a < b
*  Less than or equal to: a <= b
*  Greater than: a > b
*  Greater than or equal to: a >= b

These conditions can be used in several ways, most commonly in "if statements" and loops.
An "if statement" is written by using the `if` keyword. The condition the `if` keyword is checking, is called `expression`. Expression specifies the conditions which are based on `Boolean` expression. When a Boolean expression is evaluated it produces either a value of true or false. If the expression evaluates true the same amount of indented statement(s) following if will be executed. This group of the statement(s) is called a block.

## Indentation
> Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

## if .. else
In Python `if .. else` statement, if has two blocks, one following the expression and other following the `else` clause.
if the expression evaluates to true the same amount of indented statements(s) following if will be executed and if the expression evaluates to false the same amount of indented statements(s) following else will be executed

## else
Python evaluates each expression (i.e. the condition) one by one and if a true condition is found the statement(s) block under that expression will be executed. If no true condition is found the statement(s) block under else will be executed.
> The `else` keyword catches anything which isn't caught by the preceding conditions.

## Nested if .. else statement
In general nested if-else statement is used when we want to check more than one conditions. Conditions are executed from top to bottom and check each condition whether it evaluates to true or not. If a true condition is found the statement(s) block associated with the condition executes otherwise it goes to next condition.
