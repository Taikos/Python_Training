import time

def ft_progress(listy):
    for i in range(len(listy)):
        print("elapsed time{0: 4.2f}s".format(len(listy) - (i * 0.01)), "ETA: {0: 4.2f}s".format(i * 0.01),"[  {}%]".format(i+1) , "[",(round(i / len(listy) * 10)) * '=' + '>\033[1A\r')
        yield i

if __name__ == '__main__':
    listy = range(100)
    ret = 0
    print(ret)
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)