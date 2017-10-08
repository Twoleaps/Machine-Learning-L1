class Data():
    def __init__(self, data): # initialize the class with some data (be it int, string, list)
        self.data = data # keep a generic name to attributes it can be string, int, list, any data type
        self.type = self.get_type()

    def get_type(self):
        """"
        assign type attribute
        """
        if isinstance(self.data, str): return 'string' 
        if isinstance(self.data, int): return 'int'
        if isinstance(self.data, list): return 'list'

    def concat_data(self,a):
        try:
            return self.data + a
        except:
            return None

    def reverse_data(self):
        x=isinstance(self.data,int)
        if x is True: # proper way to check for True and False in Python
            return None
        else:
            return self.data[::-1]
            
    def return_last(self):
        x=isinstance(a,int)
        if x is True:
            return None
        else:
            return self.data[-1]

    def comparator(self,a):
         x=isinstance(self.data,int)
         y=isinstance(a,int)
         if(x is True or y is True):
            return None
         else:
            return self.data==a

    def mixture(self,a):
        x=isinstance(self.data,int)
        y=isinstance(a,int)
        if(x is True or y is True):
            return None
        else:
            p=''.join([self.data, a])
            return p
            
        
if __name__ == "__main__":
    x=Data("Python")
    a=x.concat_data(" 2.7")
    print(a)
    b=x.concat_data(1)
    print(b)
    c=x.return_last()
    print(c)
    print(x.comparator("Python"))
    print(x.comparator("abc"))
