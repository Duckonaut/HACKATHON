import time

def measure_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        measured_time = end-start
        print(measured_time)
    
    return inner
