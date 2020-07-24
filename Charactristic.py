
print("---------Python program---------");

print("Demonstration of characteristics of Class");

class Demo:
	x=10;		# class variable
	
	def __init__(self,no1,no2):
		self.i=no1;		# instance variable i and j
		self.j=no2;

obj1=Demo(10,20);
obj2=Demo(11,21);

print(obj1.i);
print(obj2.i);

print(obj1.j);
print(obj2.j);

####////////////////////////////////////////////////
## output:
##	---------Python program---------
##	Demonstration of characteristics of Class
##	10
##	11
##	20
##	21
####///////////////////////////////////////////////////
