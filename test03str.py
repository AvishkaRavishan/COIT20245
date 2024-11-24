def new1(a):
  for x in range (a):
    print(''*(a-x-1)+'*'*(2*x+1))

def new2(a):
  for x in range (a):
    print(' '*(a-x-1)+'*'*(2*x+1))

def new3(a):
  for x in range (a):
    print('  '*(a-x-1)+'*'*(2*x+1))

new1(5)
new2(5)
new3(5)
