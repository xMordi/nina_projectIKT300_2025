from multiprocessing import Process
import time

def plugin():
    print("Plugin started")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    process = Process(target=plugin)
    process.start()
    print(process.is_alive())
    time.sleep(5)

    process.terminate()
    process.join()