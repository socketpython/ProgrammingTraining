import time
import threading

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping")


threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
