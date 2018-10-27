#Fibonacci Sequence
print("Please enter the length of your fibonacci sequence: ")
end, start, length = 0 , 0 , int(input())
fibonacci = [1, 1]
for i in range(length - 2):
    if end != (length - 2):
        fibonacci.append(fibonacci[start] + fibonacci[start + 1])
        start = start + 1
print(fibonacci)
