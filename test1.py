#!/usr/bin/python

import os
'''def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
print_directory_contents('/Users/amorris')
####  

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
print A3

for s in A0:
    print (s,A0[s])
### list comprehension

l = [1,3,4,6,7,8,9,14,15,17,19,18,11,12,1,3,14,15]
y = [ x for x in l[::2] if x%2 == 0]
print y  
v1 = '10.2.3.4.x'
v2 = '10.2.3.4.y'

ver1 = v1.split('.')
ver2 = v2.split('.')
print ver1
print ver2
flag = 'n'

for i in range ( min(len(v1),len(v2)) - 1):
    print i
    if ver1[i] == ver2[i]:
        continue
    else:
        if ver1[i] > ver2[i] :
            new = v1
        else: new = v2
        flag = 'y'
        break
if flag == 'n':
    print " both are same"
else:
    print "new %s" %  new  
cDict = {}
def get_count(ctuple):
    return (ctuple[1])

def maxcount(s):
    for c in s:
        if c in cDict:
            cDict[c] += 1
        else:
            cDict[c] = 1
    clist = cDict.items()
    print clist
    chr_items = sorted(clist, key=get_count, reverse=True)
    print chr_items[0][1] 
    return(chr_items[0][1])

print maxcount("aaddeeee_rtt")  '''

def print_employee(nDict,blist):
    if not blist or not nDict: return
    newblist = []
    for boss in blist:
        for key in nDict.keys():
            if nDict[key]['boss'] == boss:
                print key, nDict[key]['boss'], nDict[key]['pos'], nDict[key]['year']
                newblist.append(key)
                del nDict[key]
    print_employee(nDict,newblist)

nDict = {}
strq = "jojo,Fred, developer, 2010/Sam, Ian, technical lead, 2009 / Ian, NULL, CEO,2007/Fred, Sam, developer, 2010/Ted, Sam, developer, 2010/tito,jojo,tse,2012"
lq = strq.split('/')
for name in lq:
    (name, boss, pos, year) = name.split(',')
    name = name.strip()
    nDict[name] = {}
    nDict[name]['boss'] = boss.strip()
    nDict[name]['pos'] = pos.strip()
    nDict[name]['year'] = year.strip()
print nDict
for key in nDict.keys():
    if nDict[key]['boss'] == 'NULL':
        print key, nDict[key]['pos'], nDict[key]['year']
        bigboss = key
        del nDict[key]
        break
blist = [bigboss]
print_employee(nDict,blist)




'''#find the number of zeros in a sorted matrix
#
m = [[0,0,0,1],[0,0,1,1],[0,1,1,1],[1,1,1,1]]
row = len(m[0])-1
col = 0 
zcnt = 0
print row,col
while col < len(m[0]):
    while m[row][col] != 0:
        row -= 1 
        if row < 0:
            break
    zcnt += row +1
    col += 1

print zcnt   

# Declare a list 
x = [2, 3, 4, 5, 6]
 
# Perform the same operation as  in above post
y = map(lambda v : v * 5, filter(lambda u : u % 2, x))
print y
out = [ x*x for x in range(5)]    
print out      

num = '343434999'
rnum = num[::-1]
print rnum
nlist = list(rnum)
print nlist
carry = 0
for  i in range (len(nlist)):
    if i == 0:
        print nlist[i]
	print int(nlist[i])
        d = int(nlist[i])
        d += 1
        print d
    else:
        d = int(nlist[i])
        d += carry 
        carry = 1
    if d < 10:
        nlist[i] = str(d)
        break
    else:
        nlist[i] = '0'
        carry = 1
if carry == 1:
    nlist.append('1')
print nlist
newrnum = ''.join(nlist)
rrnum = newrnum[::-1]
print rrnum   

x= [1,3,4,5,6,7,8,9,0,12,13,14,15]
print x
out = [n for n in x[::2] if n%2 == 0]
print out  

a_tuple = (1,2,3,4,5)
print a_tuple[3]
res = a_tuple[3]+100

a_tuple = (1,2,3,res,5) 
print a_tuple[3]  

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.items: return none
        return self.items[-1]
class stackMax(Stack):
    def max(self):
        if not self.items: return none
        return max(self.items)
b = stackMax()
b.push(30)
b.push(40)
b.push(50)
print b.pop()
print b.peek()
print b.max()    

def find_factorial(n):

    if n == 1 :
        return n
    else:
        print n
        return n*find_factorial(n-1)
print find_factorial(6)   

def check_if_prime_number(n):
    if n > 1:
        for i in range(2,n/2):
            if n % i == 0:
                print " n not prime"
                break
        else:
                print " n is  prime"
    else:
          print " n is less than 1"

check_if_prime_number(29)    

num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")    

#An Armstrong number, also known as narcissistic number, is a number that is equal to the sum of the cubes of its own
# digits. For example, 371 is an Armstrong number since 371 = 3*3*3 + 7*7*7 + 1*1*1.

lower = int(input (" enter lower range:  "))
upper = int(input (" enter upper range:  "))
print lower, upper
for num in range(lower,upper+1):
    sum = 0
    tmp = num
    while tmp > 0:
        digit =  tmp % 10
        tmp = tmp/10
        sum += digit ** 3
    if sum == num:
        print " %s Armstrong number" % num

#SIP Session initiation protocol - is a communication protocol for signalling and controlling
# multimedia communication sessions especially voice and video calls over internet.
SIP is an application layer protocol.
 SIP server only handles call setup and tear down. When both endpoinds are agreed to exchange data,
actual data is being sent using RTP  


handshake in setup:

caller                callee

-->  invite
      <----- 180 Ringing
      <-----  200 ok

-----> ACK

<===================Both way RTP Media  ========>

<---------------BYE
-----------------> 200 OK


SIP Registration:

endpoint               SIP Server

----------Register     ---->
<--------401 Unauthorized  ---
--------Register      ------>
<----------200OK    ----   


l = range(100)
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        print "fuzzbuzz"
    elif i % 3 == 0:
        print "buzz"
    elif i % 5 == 0: print "buzz"
    else:print i  

def McNuggets(n):
    ret = False
    if  n < 1:
        return False
    if (n % 6 == 0) or (n % 9 == 0) or (n % 20 == 0):
        return True
    if  (ret == False) and (n >20):
        ret = McNuggets(n-20)
    if  (ret == False) and (n >9):
        ret = McNuggets(n-9)
    if  (ret == False) and (n >6):
        ret = McNuggets(n-6)
    return ret
n = int( input("enter number:  "))
t = McNuggets(n)
print t '''

