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

    def add_compound(self, element):
        self.compounds.append(element)

    def get_result(self):
        return self.result

    def get_compounds(self):
        return self.compounds

    def get_compounds_byfactor(self, amount_needed):
        dummy_compounds = []
        factor = self.calculate_factor(amount_needed)
        for compound in self.compounds:
            new_name = compound.name
            new_amount = compound.quantity * factor
            new_element = Element(new_name, new_amount)
            dummy_compounds.append(new_element)
        return dummy_compounds

    def calculate_factor(self, amount_needed):
        if amount_needed % self.result.quantity == 0:
            factor = amount_needed / self.result.quantity
        else:
            factor = int(amount_needed / self.result.quantity) + 1
        return factor


class Chemist:

    @staticmethod
    def parse_input(file):
        formulas = []
        for line in Utility.read_linestxt(file):
            formula = Formula()
            compounds, result = line.split("=>")

            result_element = Chemist.string_to_element(result)
            formula.set_result(result_element)
            for element_line in compounds.split(","):
                formula.add_compound(Chemist.string_to_element(element_line))
            formulas.append(formula)
        return formulas

    @staticmethod
    def string_to_element(text_line):
        quanitity, name = text_line.split()
        return Element(name, int(quanitity))

    @staticmethod
    def get_compounds(formulas, wanted_result, wanted_result_amount):
        for formula in formulas:
            if formula.get_result().name == wanted_result:
                return formula.get_compounds_byfactor(wanted_result_amount)


    @staticmethod
    def add_compounds(original_list, new_items):
        for item in new_items:
            item_found = False
            for element in original_list:
                if item.name == element.name:
                    element.quantity += item.quantity
                    item_found = True
            if not item_found:
                original_list.append(item)

    @staticmethod
    def removes_element(elements, name):
        for element in elements:
            if element.name == name:
                placeholder_element = element
                elements.remove(element)
                return placeholder_element
        return Element('NONE', 0)


f = open("fourteenth.txt", "r")
formulas = Chemist.parse_input(f)

# Doing Calculations
queue = Chemist.get_compounds(formulas, "FUEL", 1)
amount = 0

while queue:
    if queue[0].name == 'ORE':
        amount += queue[0].quantity
        queue.pop(0)
    else:
        new_compounds = Chemist.get_compounds(formulas, queue[0].name, queue[0].quantity)
        queue.pop(0)
        Chemist.add_compounds(queue, new_compounds)

Utility.print_solution(int(amount), 0)
