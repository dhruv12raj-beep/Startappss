# Create a Computer class containing a CPU class using composition.


class Computer:
    def __init__(self, model):
        self.model = model
        self.cpu = CPU("i7")


class CPU:
    def __init__(self,name):
        self.name = name

c = Computer("Lenovo")
print(f"Computer model : {c.model}  -> CPU : {c.cpu.name}")
