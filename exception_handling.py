numerator = int(input("Enter the numerator:"))
denominator = int(input("Enter the denominator:"))

try :
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print("Zero is Progibited")
