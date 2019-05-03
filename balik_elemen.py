list = ['ani', 'budi', 'caca']

def listBalik():
    dump = []
    for item in range(1, len(list)+1):
        index = item * -1
        dump.append(list[index])
    return dump

print(listBalik())
