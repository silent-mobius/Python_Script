#!/usr/bin/env python3

import time
seconds = time.time()
print("Seconds since epoch =", seconds)	


seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)



print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")


named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

print(time_string)


while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(1)