def fibonacci(vorigevorige = 0,vorige = 1,max = 20):
    for math in range(max):
        print(vorigevorige)
        volgende = vorigevorige + vorige
        vorigevorige = vorige
        vorige = volgende

fibonacci(0,1,20)

# list = [0,1,1,2,3,5,8,13,21] 