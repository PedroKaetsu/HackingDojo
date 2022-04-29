import sys 

args = sys.argv

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if args[1] == 'soma':
    result = soma(int(args[2]), int(args[3]))
    print(result)
elif args[1] == 'sub':
    result = sub(int(args[2]), int(args[3]))
    print(result)
else:
    print('Syntax Error')