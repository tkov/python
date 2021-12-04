import time
import threading

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

t1 = threading.Thread(target=do_something) # pass in the function -- unexecuted
t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()   # wait to continue 
# t2.join() 

# do_something()
# do_something()

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')

