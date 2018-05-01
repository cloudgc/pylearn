##练习七 队列与堆栈
q = []


def queuePut():
    for i in range(20):
        no = "no.%s" % i
        q.append(no)
        print("put:{}".format(no), q)


queuePut()


def queueGet():
    while True:
        if len(q) == 0:
            print("exit")
            break
        else:
            data = q[0]
            del q[0]
            print("get:{}".format(data), q)


queueGet()
