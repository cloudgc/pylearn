import queue
import threading
import time

exitFlag = 0

queueLock = threading.Lock()
workQueue = queue.Queue(10)


def process_data(name, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing %s " % (name, q))
        else:
            queueLock.release()
        time.sleep(1)


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开启线程：" + self.name)
        process_data(self.name, self.q)
        print("退出线程：" + self.name)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
threads = []
threadID = 1

for subThread in threadList:
    thread = myThread(threadID, subThread, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
