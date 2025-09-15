try:
    age = int(input("enter your age:"))
    if age < 0:
        raise ValueError ("age cannot be Negative.")
    print(f"You are {age} years old.")
except ValueError as e:
    print("ValueError:",e)
finally:
    print("finished checking age.")
