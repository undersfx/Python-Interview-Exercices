import threading, random, time

# Função Worker é a que será criada varias instancias em threads diferentes
def worker(num, sleep):
    print('Worker #{} starts to sleep {} seconds '.format(num, sleep))
    time.sleep(sleep)
    print('Worker #{} woke up '.format(num))
    return

threads = []

for i in range(5):
    sleep_time = random.randint(1,5)
    t = threading.Thread(target=worker, args=(i, sleep_time,)) # Cria nova thread
    threads.append(t) # Salva a thread numa lista para ação posterior
    t.start() # Starta a thread

for t in threads:
    t.join()
