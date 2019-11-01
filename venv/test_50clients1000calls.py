"""A module for runnin the client an N processes"""
from multiprocessing import Process
import test_1000calls

if __name__ == "__main__":
    COUNT = 50
    PROCESSES = {}
    for x in range(COUNT):
        PROCESSES[x] = Process(target=test_1000calls.run)

    for x in range(COUNT):
        PROCESSES[x].start()