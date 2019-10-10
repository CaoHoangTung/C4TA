s = input("Moi ban nhap chuoi ngoac: ")

wait = []

is_valid = True

for v in s:
    if (v == '('):
        wait.append(v)
    elif (v == ')'):
        if (len(wait) == 0):
            is_valid = False
            break
        else:
            wait.pop()
    else:
        is_valid = False
        break   

if (is_valid and len(wait) > 0):
    is_valid = False
    
if (is_valid):
    print("Day ngoac hop le")
else:
    print("Day ngoac khong hop le")