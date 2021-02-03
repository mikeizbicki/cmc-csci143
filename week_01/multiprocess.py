import time
import multiprocessing
 
def heavy(n, myid):
    sum = 0
    for x in range(1, n):
        for y in range(1, n):
            sum += x**y
    print(myid, 'is done')
 
def doit(n):
    heavy(500, n)
 
if __name__ == "__main__":
    start = time.time()
    with multiprocessing.Pool() as pool:
        list(map(doit, list(range(20))))
    end = time.time()
    print("Took: ", end - start)
