# Implement a custom iterator that traverses a string in reverse order.


class Reverse:

    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.index >= 0:
            value = self.text[self.index] 
            self.index -= 1
            return value

        raise StopIteration


obj = Reverse("Python")

for ch in obj:
    print(ch)