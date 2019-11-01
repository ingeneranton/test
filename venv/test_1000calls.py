import os
import time
import test_exportCampus
import test_exportUnassignedGateways
import test_importCampus

def run():
    response = 0
    pid = os.getpid()
    while True:
        try:
            start = time.time()
            test_exportUnassignedGateways.run()
            test_exportCampus.run()
            response = int(test_importCampus.run())
            if response % 1000 ==0:
                print(
                   "%.4f : resp=%s : procid=%i"
                    % (time.time() - start, response, pid)
                    )
            time.sleep(0.001)
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            channel.unsubscribe(close)
            exit()


if __name__ == "__main__":
    run()