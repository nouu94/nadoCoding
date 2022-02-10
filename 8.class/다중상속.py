class ParentA : 
    def __init__(self, name) : 
        self.name = name 

    def whois(self) : 
        print("my name is {0} " .format(self.name))


class ChildA(ParentA) : 
    def __init__(self, name) : 
        self.name = name 

    def whois(self) : 
        print("my parent name is {0} " .format(self.name))
    

parentA = ParentA("A")
parentA.whois() # my name is A

childA = ChildA("A")
childA.whois() # my parent name is A