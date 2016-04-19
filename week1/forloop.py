someNumbers = {1: "one", 2: "two",3: "three", 4: "four"}

for (num, english) in someNumbers.items():
    if num == 3:
        continue
    print("My num is: " + str(num))
    print("My value is: " + english)

for num in range(0,20):
    if not num % 3:
        continue
    print(str(num))
