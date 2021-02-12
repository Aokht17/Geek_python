#  итератор, повторяющий элементы некоторого списка, определенного заранее
import argparse
from itertools import cycle

parser = argparse.ArgumentParser()
parser.add_argument('--threshold', type=int, help='how many times to repeat the phrase')
args = parser.parse_args()

c = 0
if args.threshold <= 0:
    print('threshold must be positive integer')
for el in cycle('maybe_enough?'):
    c += 1
    if c > args.threshold * 13:
        break
    print(el, end='')
