import time

timer = time.time()
for i in range(5):
    print(i)
    time.sleep(1)

print(f'{time.time() - timer}, seconds')
print(time.time())