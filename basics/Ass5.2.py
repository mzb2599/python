list = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        val = float(num)
        list.append(val)
    except:
        print('Invalid input')
print(list)
smallest = list[0]
largest = list[0]
for x in list:
    if x > largest:
        largest = x
    if x < smallest:
        smallest = x
print("Maximum", int(largest))
print("Minimum", int(smallest))
