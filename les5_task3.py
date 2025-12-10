import time

M = int(input('Введите кол-во повторов первого цикла'))
N = int(input('Введите кол-во повторов второго цикла'))

timer = time.time()
for i in range(M):
    for i in range(N):
        print(i)
        time.sleep(1)

print(time.time() - timer, 'секунд')