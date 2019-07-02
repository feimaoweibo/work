import threading
import time
import queue
class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # qsize 返回queue内容长度
            if queue.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = "生成产品" + str(count)
                    # put 是往queue中放入一个值
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)
