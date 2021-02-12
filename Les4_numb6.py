#  итератор, генерирующий целые числа, начиная с указанного
import argparse
from itertools import count

parser = argparse.ArgumentParser()
parser.add_argument('--threshold_low', type=int, help='the smallest number')
parser.add_argument('--threshold_up', type=int, help='the biggest number')
args = parser.parse_args()

for el in count(args.threshold_low):
    if el > args.threshold_up:
        break
    print(el)
