hours = input()

if hours.isdigit():
    hours = int(hours)

    if hours <= 2:
        print(hours * 100)
    elif hours <= 5:
        print((2 * 100) + (hours - 2) * 50)
    else:
        print((2 * 100) + (3 * 50) + (hours - 5) * 20)
else:
    print("error")