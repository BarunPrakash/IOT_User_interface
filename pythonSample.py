# Python code 
# Designed By Barun
# objective  to remember  syntax utility!!

1. Start Learn

print "Barun Hi"
**************************************
2. conditional 

if True:
	print "yes"
else:
	print "No!!"
************************************
#Assiging Value into variable

age =20
income =20.5
name ="Barun"

print age
print income
print name
*************************************
#python data Types Number ,string ,list, Tuple ,Dictionary

# string
str ="Barun prakash"
print str[0]
print str[2:5]
print str[3:]
print str*2
print str + "Test"
*****************************
#python data Types Number ,string ,list, Tuple ,Dictionary

# list is a containter of different data type ,denoted by []
str =["Barun prakash",29, 50000.50]
test =[2,5,"KK"]
print str  # print complete list
print str[0] #print first element
print str[1:2] #print one to 2 
print str[1:]  #print element from 1
print str*2     # print list two time 
print str + test  # Add two different list "concatenated"
***********************************************
#python data Types Number ,string ,list, Tuple ,Dictionary

# Tuple is a containter of different data type ,denoted by () ,size cann't be changed
#it can be thought of read only memory
str =("Barun prakash",29, 50000.50)
test =[2,5,"KK"]
print str  # print complete list
print str[0] #print first element
print str[1:2] #print one to 2 
print str[1:]  #print element from 1
print str*2     # print list two time 
print str + test  # Add two different list "concatenated"
*****************************************************************************

# Dictionary is a  Hash containter of different data type ,denoted by ()

str ={Name:"Barun prakas",Age:29, income:50000.50}
test =[2,5,"KK"]
print str  # print complete list
print str[0] #print first element
print str.keys()     # print all key 
print str.values()  # print value
********************************************************************

#single statment 

var =40
if(var ==40):
	print "OK!!"

print "Good bye!!"
**********************************************************************
#for loop

fruits = ["apple","banana","cherry"]
str ="Barun"
for x in fruits:
	print(x);
for x in "barun":
	print(x);
********************************************************
#for loop

fruits = ["apple","banana","cherry"]

for x in fruits:
	if x=="cherry":
		print "It is available"
		break

for x in range(10):
			print(x)
		
*************************************************************	
#function 
def addTwoNum(x,y):
	return(x+y);

		
	
	

print(addTwoNum(2,4))

******************************************************
#class
def test(x,y):
	return(x-y)
	
	
#ef main():
#	print(test(4,2))
		
class barunContainer:
	count=0
	def __init__(self,name,salary):
		self.name =name
		self.salary=salary
		barunContainer.count+=1
		
		
	def dispCount(self):
		print "Total Employe %d" %barunContainer.count
	def dispContainer(self):
		print  "Name:",self.name,self.salary


		
#2.dispContainer()

def main():
	print(test(4,2))		
	b1= barunContainer("Barun",70)
	b2=barunContainer("karthik" ,35)
	b1.dispContainer()
	

		

if __name__ =="__main__":
	main()
***********************************************
		
