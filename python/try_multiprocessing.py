import time
from random import randint
from multiprocessing import Pool


def proc(i):
    time.sleep(randint(1, 15))
    print(i)


def on_completion(result):
    print(result)


if __name__ == "__main__":
    pool = Pool(10)
    # results = [pool.apply_async(proc, args=(i,), callback=on_completion) for i in range(10)]
    results = [pool.apply_async(proc, args=(i,)) for i in range(10)]
    pool.close()
    pool.join()  # wait for worker processes to exit
