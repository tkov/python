# using concurrent.futures

import concurrent.futures
import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'       # changed to a return statement

with concurrent.futures.ThreadPoolExecutor() as executor:
    # EXAMPLE 1 
    # executing one function at a time
    # f1 = executor.submit(do_something, 1)   # do_something with argument of 1
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())


    secs = [5,4,3,2,1]

    # EXAMPLE 2
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # EXAMPLE 3
    results = executor.map(do_something, secs)  # map returns results in the order they were started

    for result in results:
        print(result)


# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')