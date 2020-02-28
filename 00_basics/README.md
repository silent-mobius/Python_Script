# Python Script Basics

## Hardware -> CPU/RAM

## RAM -> management -> Programming

## Software Development

### Compile

#### C, C++ or C# 

The difference between compile time and run time is an example of what pointy-headed theorists call the phase distinction. It is one of the hardest concepts to learn, especially for people without much background in programming languages. To approach this problem, I find it helpful to ask

- What invariants does the program satisfy?
- What can go wrong in this phase?
- If the phase succeeds, what are the postconditions (what do we know)?
- What are the inputs and outputs, if any?

### Compile Time Environment 

The program need not satisfy any invariants. In fact, it needn't be a well-formed program at all. You could feed this HTML to the compiler and watch it barf...
- What can go wrong at compile time:
  - Syntax errors
  - Typechecking errors
  - (Rarely) compiler crashes
- If the compiler succeeds, what do we know?
  - The program was well formed---a meaningful program in whatever language.
  - It's possible to start running the program. (The program might fail immediately, but at least we can try.)
- What are the inputs and outputs?
  - Input was the program being compiled, plus any header files, interfaces, libraries, or other voodoo that it needed to import in order to get compiled.
  - Output is hopefully assembly code or relocatable object code or even an executable program. Or if something goes wrong, output is a bunch of error messages.

### Run Time Environment

#### JavaScript, Bash or Python 

We know nothing about the program's invariants---they are whatever the programmer put in. Run-time invariants are rarely enforced by the compiler alone; it needs help from the programmer.

- What can go wrong are run-time errors:
  - Division by zero
  - Dereferencing a null pointer
  - Running out of memory
  
- Also there can be errors that are detected by the program itself:
  - Trying to open a file that isn't there
  - Trying find a web page and discovering that an alleged URL is not well formed
  
- If run-time succeeds, the program finishes (or keeps going) without crashing.
  - Inputs and outputs are entirely up to the programmer. Files, windows on the screen, network packets, jobs sent to the printer, you name it. If the program launches missiles, that's an output, and it happens only at run time :-)




## REPL - Read Evaluate Print Loop


## Keywords and Identifiers

*_Keywords in Python_*

False |	class | finally | is | return
----- | ------ | ------- | ---- | ----
None 	|continue |	for 	| lambda |	try
True 	| def |	from |	nonlocal |	while
and 	| del |	global | 	not |	with
as |	elif | 	if |	or |	yield
assert |	else |	import  |	pass  	 
break |	except |	in |	raise | is

