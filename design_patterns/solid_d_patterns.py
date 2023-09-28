"""
S - Single Responsibility Principle
O - Open-Close Principle
L - Liskov Substitution Principle
I - Interface Sagration Principle
D - Dependancy Inversion Principle
"""

# Single Responsibility Principle ====>

"""
One class should have only one responsibility. 
It should so manupulations for its primary responsibility and should not do multiple things.
"""

class Journal:

    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.entries.append(text)
        self.count += 1
    
    def remove_entry(self, position):
        del self.entries[position]
        self.count -= 1
    
    def __str__(self) -> str:
        return "\n".join(self.entries)

    """
    Below code violates the principle of SRP as save file or load file from web is different functionality
    We can Write a saperate class to deal with this responsibility
    """

    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass

class PersistenceManager:
    def save_to_file(journal:Journal, filename:str):
        with open(filename, "w") as fh:
            fh.write(str(Journal))

j = Journal()
j.add_entry("I studied today.")
j.add_entry("I ate an apple.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = 'journal.txt'
p.save_to_file(j, file)

#=================================Open-Close Principle=========================>
"""
- Class or Object should be open to extension but not for modification
- It states that once you developed the class, written the UTs, you should not modify the class again.
- Develope the features or classes in a such a way that if in future we have to add certain method or functionality, 
then we should write a new class by extending the old class.

"""
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARG = 3

class Product:
    def __init__(self, name, size, color) -> None:
        self.name = name
        self.size = size
        self.color = color

"""
Below class violates the OCP as if you want to add additional filter, you will have to modify it.
"""
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

"""
Below is updated cod which follows Open-Close Principle
"""
class Specification:
    def is_satisfied(self, item):
        pass

    # and operator makes life easier
    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


# class AndSpecification(Specification):
#     def __init__(self, spec1, spec2):
#         self.spec2 = spec2
#         self.spec1 = spec1
#
#     def is_satisfied(self, item):
#         return self.spec1.is_satisfied(item) and \
#                self.spec2.is_satisfied(item)

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print('Green products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
    print(f' - {p.name} is green')

# ^ BEFORE

# v AFTER
bf = BetterFilter()

print('Green products (new):')
green = ColorSpecification(Color.GREEN)
for p in bf.filter(products, green):
    print(f' - {p.name} is green')

print('Large products:')
large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
    print(f' - {p.name} is large')

print('Large blue items:')
# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
large_blue = large & ColorSpecification(Color.BLUE)
for p in bf.filter(products, large_blue):
    print(f' - {p.name} is large and blue')

#======================LisKov Substitution Principle================================>
