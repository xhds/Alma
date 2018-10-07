def Consumer():
    yCode = ""
    while True:
        receiveObj = yield yCode
        if not receiveObj:
            return
        print("Consumer receive %d" % receiveObj)
        yCode = "Consumer Finish"

def Producer(consumer):
    consumer.send(None)
    i = 0
    while i < 5:
        i += 1
        print("Producing %d" % i)
        r = consumer.send(i)
        print("Consumer return %s" % r)
    print("Produce Done")
    consumer.close()

c = Consumer()
Producer(c)
