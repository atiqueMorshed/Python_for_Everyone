largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = float(num)
        except:
            print("Invalid input")
            continue
        if largest is None:
            largest = num
            smallest = num
        elif largest < num:
            largest = num
        elif smallest > num:
            smallest = num
print("Maximum is", int(largest))
print("Minimum is", int(smallest))
