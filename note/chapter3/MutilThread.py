import time
import _thread
import threading

#
#
# def printT1(threadname):
#     count = 1
#
#     while count < 5:
#         time.sleep(1)
#         count += 1
#         print("this is my thread:", threadname, count, ">>>")
#
#
# try:
#     _thread.start_new_thread(printT1, ("Thad1",))
#     _thread.start_new_thread(printT1, ("Thad2",))
# except:
#     print("error thread")
#
# while True:
#     time.sleep(1)
#     print(threading.active_count())

exitFlag = 0

threadLock = threading.Lock()


def printTime(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("{}: {} ".format(threadName, time.ctime(time.time())))
        counter -= 1


class myThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print("thread start {}".format(self.name))
        threadLock.acquire()
        printTime(self.name, self.counter, 3)
        threadLock.release()


threads = []

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

threads.append(thread1)
threads.append(thread2)
thread1.start()
thread2.start()

for t in threads:
    t.join()
print("main processs exit ")
