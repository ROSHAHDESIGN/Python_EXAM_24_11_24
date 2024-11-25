# for loop

# •	N – цяло число – 0 <= N < M
# •	M – цяло число – N < M <= 10000
# S – цяло числo – N <= S <= M
n = int(input())
m = int(input())
s = int(input())


for num in range(m, n + 1, -1):
    if num == s and (num % 2 == 0 and num % 3 == 0):
        break


    elif num % 2 == 0 and num % 3 == 0:
        print(f"{num}" , end=" ")
        num += 1




