#%% time section as introduction
# how does this work?
# import time lib to calculate time needed for function to work
import time
# fill "start" variable with time counter, this will return float value
start = time.perf_counter()
# create basic function that need to do some stuff, this will print before action, sleep for 1s and print anfter 1 s of sleep
def work_function():
    print("waith ")
    time.sleep(1)
    print("done waiting")
#call function without arguments because there is no 
work_function()
# fill "finish" variable with time counter, this will return float value
finish = time.perf_counter()
# print total time, round will show only 2 decimals
total_time = finish - start
# print out total time, and round to 4 numbers after dot
print(f"time to finish: {round(total_time, 4)} seconds")
# this can be done in one line {round(start-finish, 4)} but this is more readable


#%% introduction to threading 
import time
# import threading module, it is ins stdlib
import threading
start = time.perf_counter()
def work_function():
    print("waith 1s")
    time.sleep(1)
    print("done waiting")
#work_function()
thread_01 = threading.Thread(target=work_function)
thread_02 = threading.Thread(target=work_function)

# now we have 2 thread object but you need to start threads as well
thread_01.start()
thread_02.start()
# if you dont join in, script will go to last print statement without finishing threads so it will not print out "done waiting"
thread_01.join()
thread_02.join()

finish = time.perf_counter()
total_time = finish - start
print(f"time to finish: {round(total_time, 4)} seconds")


# %% now lets create loop for this threads that will do it 10 times
import time
import threading
start = time.perf_counter()
def work_function():
    print("waith 1s")
    time.sleep(1)
    print("done waiting")
thread_list = []
# create loop "_" means empty variable, it will not be used
for _ in range(10):
# if you leave like this it will not, you can't use join in a loop because it will loop and finish threads one by one, just try it, it will not write out "done waiting"
    threads = threading.Thread(target=work_function)
    threads.start()
# to solve problem you need to create empty list and append "thread_list" to it
    thread_list.append(threads)
# now lets gi through list and join threads to finish them
for thread in thread_list:
    thread.join()

finish = time.perf_counter()
total_time = finish - start
print(f"time to finish: {round(total_time, 4)} seconds")

#%% How to pass an argument to a function
import time
import threading
start = time.perf_counter()
# pass arg in to the function
def work_function(time_var):
    print(f"waint for {time_var} sec")
    time.sleep(time_var)
    print("done waiting")
thread_list = []
for _ in range(10):
# to thread, add and argument list, this will fill function argument
    threads = threading.Thread(target=work_function, args=[1.75])
    threads.start()
    thread_list.append(threads)

for thread in thread_list:
    thread.join()

finish = time.perf_counter()
total_time = finish - start
print(f"time to finish: {round(total_time, 4)} seconds")



# %% lets see what threadPoolExecutor do
import time
# thread pool executor is in concurrent.futures module
import concurrent.futures
start = time.perf_counter()
# pass arg in to the function
def work_function(time_var):
    print(f"waint for {time_var} sec")
    time.sleep(time_var)
    return "done waiting"
#    print("done waiting"), insted of print, return result to 

with concurrent.futures.ThreadPoolExecutor() as executor:
# with executor there is coulpe of things you can do
# for executing function once at the time, "use submit" method, this will schedule function to be executed and it will return future object
    f1 = executor.submit(work_function, 1) # submit function with arg 1
# future object encapsulete execution of and allow to check state of the function, including result, if you grab result it will give return value of the function
# lets print results, that will waith untill function is complete, than print out

# if there is a need to execute multiple times, just add another submit
    f2 = executor.submit(work_function, 1)
    print(f1.result())
    print(f2.result())

finish = time.perf_counter()
total_time = finish - start
print(f"time to finish: {round(total_time, 4)} seconds")

# %% 
import time
import concurrent.futures
start = time.perf_counter()

def work_function(time_var):
    print(f"waint for {time_var} sec")
    time.sleep(time_var)
#    return "done waiting"
# if you want to see what function finish firs just add arg in a return
    return f"done waithin in {time_var} seconds"

with concurrent.futures.ThreadPoolExecutor() as executor:
# now lets create list of values
    seconds = [5,4,3,2,1]
# this will submit 5 times to a function with each elemt of a list as an argumet
    results = [executor.submit(work_function, sec) for sec in seconds]
# lets create loop function that will create 10 separate threads for function with arg 1
    #results = [executor.submit(work_function, 1) for seconds in range(10)]

# to get this results call "ascompleted" this will give a iterator that we can loop over that it will yield result of a threads as they complete
    for f in concurrent.futures.as_completed(results):
        print(f.result())
# if you dont have this function will not print "Done waithing"


finish = time.perf_counter()
total_time = finish - start
print(f"time to finish: {round(total_time, 4)} seconds")

# %% this is also possible to do with python map method
import time
import concurrent.futures
start = time.perf_counter()

def work_function(time_var):
    print(f"waint for {time_var} sec")
    time.sleep(time_var)
    return f"done waithin in {time_var} seconds"

with concurrent.futures.ThreadPoolExecutor() as executor:

    seconds = [5,4,3,2,1]
# map fucntions, and iterate it over every value from the list
    results = executor.map(work_function, seconds)
# as submit returned future object, map will return results, map will return results in order they started 
# lets make a loop
    for result in results:
        print(result)
# difference is that when you return results it will return after first task is finish
# if function need to reise exception, it will be reised when its value is retrieved from results iterator
finish = time.perf_counter()
total_time = finish - start
print(f"time to finish: {round(total_time, 4)} seconds")
# %%
