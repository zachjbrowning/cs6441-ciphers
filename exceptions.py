class exception:
    def __init__(self, name, description):
        self.type = name 
        self.description = description

    def __str__(self):
        return self.name
    
