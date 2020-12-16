#!/usr/bin/python

input_range = "367479-893698"
input_range = list(map(int, input_range.split("-")))
nb_passwords1 = 0
nb_passwords2 = 0

def test_password1(p):
    two_identical_digits = False
    ps = str(p)
    if len(ps) != 6:
        return False
    for i in range(len(ps)-1):
        if ps[i] == ps[i+1]:
            two_identical_digits = True
        if int(ps[i+1]) < int(ps[i]):
            return False
    return two_identical_digits

def test_password2(p):
    digits = {}
    ps = str(p)
    if len(ps) != 6:
        return False
    for i in range(len(ps)):
        if ps[i] in digits:
            digits[ps[i]] += 1
        else:
            digits[ps[i]] = 1
        if i == len(ps) - 1:
            break
        if int(ps[i+1]) < int(ps[i]):
            return False
    if 2 in digits.values():
        return True
    else:
        return False

for p in range(input_range[0],input_range[1]+1):
    if test_password1(p) is True:
        nb_passwords1 += 1
    if test_password2(p) is True:
        nb_passwords2 += 1

print("Part 1:", nb_passwords1)
print("Part 2:", nb_passwords2)

#for p in [122345,111123,135679,111111,223450,123789,12344,135799,112233,123444,111122]:
#    print(p," >>> ", end='')
#    if test_password2(p) is True:
#        print("OK")
#    else:
#        print("NOK")

    
    
        



