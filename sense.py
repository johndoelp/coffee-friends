import time


status = 0

def detect(status):
    while status is 0:
        #if current exeeds baseline avg current of:
        #the last 5sec?
        #sleep(10sec) post-boot then collect 10sec of passive current?
        #change status = 1, which sets appliance_status to active
        status = 1
        return status

        #wait 5sec until looping again
        time.sleep(5)

detect(status)