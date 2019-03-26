import multiprocessing
import time

def spawn(n):
    time.sleep(1)
    print('{} Spawned!'.format(n))

if __name__ == "__main__":
    for i in range(10):
        p = multiprocessing.Process(target=spawn, args=(i,))
        p.start()
        #p.join() #Waits until the last spawn finish to go to the next
