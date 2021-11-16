import argparse

# python argument_types.py -h
parser = argparse.ArgumentParser()

# Позиционные
parser.add_argument('a', type=int, help='First argument')
parser.add_argument('b', type=int, help='Second argument')

# Optional, именованные
parser.add_argument('-a', '--action', help='What to do with numbers?', default='sumarize')

args = parser.parse_args()
print(args)


def sumarize(a, b):
    print(a + b)


def minusize(a, b):
    print(a - b)


if args.action == 'sumarize':
    sumarize(args.a, args.b)
elif args.action == 'minusize':
    minusize(args.a, args.b)
else:
    print('Ooops')
