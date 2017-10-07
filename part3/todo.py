class todo():
    str1="python"
    str2="programming"
    def type(self):
        type_name=type(todo.str1)
        print(type_name)

    def concat_data(self,a,b):
        s=""
        try:
            return s+a+b
        except:
            return None
    def reverse_data(self,a):
        x=isinstance(a,int)
        if x== True:
            return None
        else:
            return a[::-1]
            
            
    def return_last(self,a):
        x=isinstance(a,int)
        if x == True:
            return None
        else:
            return a[-1]

    def comparator(self,a,b):
         x=isinstance(a,int)
         y=isinstance(a,int)
         if(x == True or y == True):
            return None
         else:
            return a==b
    def mixture(self,a,b):
        x=isinstance(a,int)
        y=isinstance(a,int)
        if(x == True or y == True):
            return None
        else:
            p=''.join(b)
            return a+p
            
        
    
        
        

x=todo()
x.type()
a=x.concat_data("hello"," this works!")
print(a)
b=x.concat_data(1,2)
print(b)
y=[1,2,3,4,5]
c=x.return_last(y)
print(c)
c=x.return_last("abc")
print(c)
c=x.return_last(1)
print(c)
print(x.comparator(y,y))
print(x.comparator("abc","xyz"))
print(x.comparator(1,2))
print(x.mixture("aa",['b','b']))
print(x.reverse_data("abcd"))
print(x.reverse_data(y))
