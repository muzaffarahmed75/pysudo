from time import *
from textwrap import *
def w(s): print fill(s,77)
print '='*77+'\n'+'Sudoku Solver'.center(77,'-')+'\n'+'='*77
w("This program solves Sudoku puzzles with a median solve time of 5 seconds. The program prompts for row by row input of the puzzle. The input must be a nine-digit number and must not contain any characters other than digits. 0 must be used to denote empty cells.")
w("The stored input can be edited by entering 'edit' without quotes at any input prompt. 'Delete' or 'del' can be entered to delete the last input row. After entering all 9 rows, enter 'done' to confirm the input, or 'edit'/'del' to modify it. Use 'ins' to insert a row.")
print
w("The program uses a backtracking algorithm to solve, and in extremely rare and unfavorable cases the solve time can extend up to 20 minutes.")
w('_'*77)
il=[]
def p():
 w('Stored input:')
 for x in il: print ''.join([j+' ' for j in list(x)])
def p1(y):
 y=[y[i:i+9] for i in xrange(0,81,9)]
 for j,v in enumerate(y):
  v=list(v)
  v.insert(3,'| ')
  v.insert(7,'| ')
  y[j]=''.join(v)
 for i,x in enumerate(y):
  if not i%3 and i: w('- - - + - - - + - - -')
  print ''.join(x)
def p2():
 print '\nYour Sudoku puzzle is:\n'
 y=[j+' ' for x in il for j in list(x)]
 p1(y)
 print '\nSolving...\n'
def p3():
 print '\nThe solution to your Sudoku is:\n'
 o=[map(str,y) for y in gl]
 y=[j+' ' for x in o for j in x]
 p1(y)
def ed():
 while 1:
  while 1:
   v=raw_input("\nDo you wish to edit any row?\nIf yes, enter the row number; if no, enter 0: ")
   if not(len(v)==1 and v.isdigit()):
    print "Enter a single digit integer"
    continue
   v=int(v)
   if v>len(il):
    print "Enter a valid row number. The stored input has only %d rows."%len(il)
    continue
   break
  if v:
   print "\nEditing row %d"%v
   while 1:
    i=raw_input("\nEnter row %d: "%v)
    if not(len(i)==9 and i.isdigit()):
     print "Error: invalid input"
     p()
     continue
    else:
     il[v-1]=i
     p()
    break
  else: break
def ins():
 global il
 while 1:
  r=raw_input("\nWhich row do you wish to insert? (e.g. if you want to enter a row between row 3 and row 4, enter 4. 0 to exit insert.): ")
  if not(r.isdigit() or len(r)==1):
   print "Enter a single digit integer."
   continue
  r=int(r)
  if not r: break
  if r>len(il) or r<1:
   print "Invalid input. Stored input has only %d rows."%len(il)
   continue
  print "\nInserting row %d"%r
  i=raw_input("\nEnter row %d: "%r)
  if not(len(i)==9 and i.isdigit()):
   print "Error: invalid input"
   p()
   continue
  else:
   il=il[:r-1]+[i]+il[r-1:]
   p()
  break
  
def chk(gl):
 for x in gl:
  x=[j for j in x if j]
  if len(set(x))!=len(x): return 0
 l=[a[i] for i in range(9) for a in gl]
 c=[l[i:i+9] for i in xrange(0,81,9)]
 for x in c:
  x=[j for j in x if j]
  if len(set(x))!=len(x): return 0
 l=[x for x in [a[i:i+3] for i in range(0,9,3) for a in gl]]
 b=[l[i:i+3] for i in xrange(0,27,3)]
 for x in b:
  x=sum(x,[])
  x=[j for j in x if j]
  if len(set(x))!=len(x): return 0
 return 1
#"""
while 1:
 i=raw_input("\nEnter command"+[': '," or row %d: "%(len(il)+1)][bool(9-len(il))]).lower()
 if len(il)==9:
  if i=='done': break
 if i[:3]=='del':
  il.pop()
  p()
  continue
 if i=='edit':
  ed()
  continue
 if i[:3]=='ins':
  ins()
  continue
 if not(len(i)==9 and i.isdigit()):
  print "\nError: invalid input"
  p()
  continue
 il.append(i)
 p()
ed()
#"""
#il=['000000000','000003085','001020000','000507000','004000100','090000000','500000073','002010000','000040009']
gl=[map(int,list(y)) for y in il]
while not chk(gl):
 print "\nInvalid clues. Please edit the input."
 ed()
 gl=[map(int,list(y)) for y in il]
print "\nAll clues valid." ###
t1=time()
p2()
#"""
ik=[int(x.strip('0')+'7') for x in il]
a=ik.index(max(ik))
gl,da=[map(int,list(y)) for y in il],{}
q2=[(i,j) for j in range(9) for i,v in enumerate(gl[j]) if not v]
for i,v in enumerate(q2):
 l,da[v]=[],-1
 for n in range(9,-1,-1):
  gl[v[1]][v[0]]=n
  if chk(gl): da[v]+=1
q=[i[0] for i in sorted(da.items(), key=lambda x: x[1])]
#"""
z,f=0,1
#print time()-t1
#q=[(i,j) for j in range(9) for i,v in enumerate(gl[j]) if not v]
while 1:
 i,j=q[z][0],q[z][1]
 if gl[j][i]<9:
  gl[j][i]+=1
  if chk(gl): z,f=z+1,1
 elif not chk(gl): gl[j][i],z,f=0,z-1,0
 elif f: z+=1
 else: gl[j][i],z=0,z-1
 if z==len(q) or z<0: break
 continue
p3()
print '\nSolved in %r seconds.'%round(time()-t1,3)
raw_input('\n<hit enter to exit>')
exit()
