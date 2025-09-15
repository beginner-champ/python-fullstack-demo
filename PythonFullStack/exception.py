try:
    num = int (input("Enter a number:"))
    div = num / 0
    print ("result is:", div)
except ZeroDivisionError:
    print ("Division by zero not allowed")
finally :
    print ("Exception handled")
