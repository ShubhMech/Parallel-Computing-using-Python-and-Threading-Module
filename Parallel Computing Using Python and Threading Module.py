#!/usr/bin/env python
# coding: utf-8

# ## Running the code synchronously:

# In[3]:


import time
start= time.perf_counter()

def doing():
    print("Going to sleep for a second now")
    time.sleep(1)
    print("Finished sleping")

doing()

 # Running the code again to demonstrate how synchronous function calls work

doing()
    
finish= time.perf_counter()

print(f'Finished the task in {round(finish- start, 12)} seconds' )


# #### CPU bound operations need CPU power to run and I/O bound operations don't need that much of a CPU processing powwer and mostly wait for user input/ response from the web/Reading or Writing system files.
# 
# Note: We use Threading when we need to tun tasks concurrently and use Multi-Processing when proceses are CPU bound and use parallel computing. 

# ## So we can use Threading for operations that need a lot of time just waiting and not using much CPU power.

# ![Threading.png](attachment:Threading.png)

# ### Improving upon above method to run code concurrently and subsequently printing time as before.

# In[4]:


import time, threading
start= time.perf_counter()

def doing():
    print("Going to sleep for a second now")
    time.sleep(1)
    print("Finished sleping")

thread1= threading.Thread(target= doing)
thread2= threading.Thread(target= doing)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
    
# doing()

# Running the code again to demonstrate how synchronous function calls work

# doing()
    
finish= time.perf_counter()

print(f'Finished the task in {round(finish- start, 12)} seconds' )


# #### Notice the time difference between the two code scripts.

# In[11]:


## Improving upon the code and running the 'doing' function 10 times:

import time, threading
start= time.perf_counter()

def doing():
    print("Going to sleep for a second now \n")
    time.sleep(1)
    print("Finished sleping \n")
    
threads= []
    
for thread in range(10):

    thread= threading.Thread(target= doing)
    # thread2= threading.Thread(target= doing)

    thread.start()
    # thread2.start()
    
    threads.append(thread)

    
for thread  in threads:
    
    thread.join()
    

    
# doing()

# Running the code again to demonstrate how synchronous function calls work

# doing()
    
finish= time.perf_counter()

print(f'Finished the task in {round(finish- start, 12)} seconds' )


# #### Making the code more responsive by giving the "doing" function arguments of its own

# In[2]:


## Improving upon the code and running the 'doing' function 10 times:

import time, threading
start= time.perf_counter()

def doing(seconds):
    print(f"Going to sleep for {seconds} second(s) now \n")
    time.sleep(seconds)
    print("Finished sleping \n")
    
threads= []
    
for thread in range(10):

    thread= threading.Thread(target= doing, args=[1.5])
    # thread2= threading.Thread(target= doing)

    thread.start()
    # thread2.start()
    
    threads.append(thread)

    
for thread  in threads:
    
    thread.join()
    

    
# doing()

# Running the code again to demonstrate how synchronous function calls work

# doing()
    
finish= time.perf_counter()

print(f'Finished the task in {round(finish- start, 12)} seconds' )


# In[ ]:




