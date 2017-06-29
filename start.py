from threading import Thread
from time import time, sleep
import signal
import sys
from Connection import ApiConnection


def test_get(route, api):
    r = api.get(route)
    print(r.status_code)
    #print("thread %d running the %d time" % (i))
    #sleep(1)

if __name__ == "__main__":
    endpoint = input('Endpoint: ')
    token = input('Token: ')
    reps = int(input('# repetitions: '))
    api = ApiConnection(endpoint=endpoint, token=token, test_connection=(False if token == '' else True))

    routes = ["api", "test"]
    threads = []
    t1 = time()
    rc = 0
    for i in range(0, reps):
        for r in routes:
            thread = Thread(target=test_get, args=(r, api, ))
            thread.start()
            rc += 1
            threads.append(thread)

    for t in threads:
        t.join()
    t2 = time()
    print("Executed %d requests in %2.4f seconds" % (rc, (t2-t1)))