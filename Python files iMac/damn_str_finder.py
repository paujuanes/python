# find 'xyz' not preceded by '.' and return True or False

def xyz_there(str):
    if len(str) < 3:
        return False
    else:
        for i in range(len(str)-2):
            if str[i:i+3] == 'xyz':
                if str[i-1] == '.':
                    found = False
                    continue
                else:
                    found = True
                    break
            else:
                found = False
                continue
        return found


print(xyz_there('xyz.abc'))
print(xyz_there('xyz.abc'))
print(xyz_there('xyz.abc'))