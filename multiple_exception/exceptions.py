string = input()

try: 
    num = int(input(" Enter the numbers"))
    print(string + num)
except (TypeError, ValueError) as e:
    print(e)
    