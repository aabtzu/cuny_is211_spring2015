__author__ = 'amit'

import sys

# put students work directory first for testing purposes
sys.path.insert(0,'.')

import assignment1_part1 as p1
import assignment1_part2 as p2

# test part1
ll = [ 2,3,4,5,6,7,8,9,10,11,12]


dlist = [ 2,3,4,5,12,25]


#print sys.path
print p1.listDivide(ll)

for dd in dlist:
    print p1.listDivide(ll,dd)


p1.testListDivide()

# test part2
dq = p2.Book("Cervantes","Don Quixote")
dq.display()