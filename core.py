class food:
    def __init__(self,name,weight):
        if not name.replace(" ","").isalpha():
            raise ValueError(f"The name {name} is not valid.\n make sure that the name is in English.")
        if not isinstance(weight,(int,float)):
            raise TypeError(f"Weight needs to be a number.")
        if weight<=0:
            raise ValueError(f"Illegal weight, please re-enter.")
        self.name = name
        self.weight = weight