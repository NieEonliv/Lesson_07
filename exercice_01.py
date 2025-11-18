inputString = input("Введите строку: ")
center = int(len(inputString) / 2)

if len(inputString) % 2 != 0:
    inputString = inputString[:center] + inputString[center + 1:]

reversedInputString = inputString[::-1]

print("yes" if inputString[:center] == reversedInputString[:center] else "no")
