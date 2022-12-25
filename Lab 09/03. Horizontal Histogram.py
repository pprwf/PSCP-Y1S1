'''histogram'''

def sorting(var):
    """Sort by value"""
    char = var[0]
    return ord(char) + (100 if char.isupper() else 0)

def hist(string):
    """hist function"""
    for char, count in sorted({i: string.count(i) for i in string}.items(), key=sorting):
        print(char, ":", "".join(["-" if i % 5 else "-|" for i in range(1, count+1)]).rstrip("|"))
hist(input())
