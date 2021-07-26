#type of data stored in variables
from typing import FrozenSet


x="ajay"  #string
x= 1 #int
x=20.5 #float
x=1j #complex
x=["aj","kumar","sana"] #list
x=("name","kumar","chanti") #tupple
x={"apple","cherry","grape"} #set
x=FrozenSet({"apple","banana","cherrty"}) #frozenset
x=True #bool
x= b"Hello" #bytes



x = str("Hello World")	#str	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	 #memoryview