from utility import Utility


class Element:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Formula:

    def __init__(self):
        self.compounds = []
        self.result = None

    def set_result(self, element):
        self.result = element

    def get_result(self):
        return self.result

    def get_compounds(self):
        return self.compounds

    def get_compuounds_factor(self, factor):
        dummy_compounds = []
        for compound in self.compounds:
            compound.quantity *= factor
            dummy_compounds.append(compound)
        return dummy_compounds

    def add_compound(self, element):
        self.compounds.append(element)


class Chemist:

    @staticmethod
    def string_to_element(text_line):
        quanitity, name = text_line.split()
        return Element(name, int(quanitity))

    @staticmethod
    def get_compounds(formulas, wanted_result, wanted_result_amount):
        for formula in formulas:
            if formula.get_result().name == wanted_result:
                return formula.get_compuounds_factor(wanted_result_amount)

    @staticmethod
    def removes_element(elements, name):
        for element in elements:
            if element.name == name:
                placeholder_element = element
                elements.remove(element)
                return placeholder_element
        return Element('NONE', 0)


# Parsing input
formulas = []
f = open("fourteenth.txt", "r")
for line in Utility.read_linestxt(f):
    formula = Formula()
    compounds, result = line.split("=>")

    result_element = Chemist.string_to_element(result)
    formula.set_result(result_element)
    for element_line in compounds.split(","):
        formula.add_compound(Chemist.string_to_element(element_line))

    formulas.append(formula)

queue = Chemist.get_compounds(formulas, "FUEL", 1)
amount = 0

while queue:
    iron_ore = Chemist.removes_element(queue, 'ORE')
    amount += iron_ore.quantity

    new_compounds = Chemist.get_compounds(formulas, queue[0].name, queue[0].quantity)
    queue.pop(0)
    queue = queue + new_compounds
