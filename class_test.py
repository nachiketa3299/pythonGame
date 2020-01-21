class Country:
    """
    Super Class
    """

    name = '_Country Name'
    population = '_Population'
    capital = '_Capital'

    def show(self):
        print("Country's method")


class Korea(Country):
    """
    Sub Class
    """

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print('Country name is:', self.name)


class Human:
    """
    Super Class
    """
    name = "_human_name"
    weight = 0
    height = 0
    
    def human_info(self):
        print('- name:/t', name)
        print('- weight:/t', weight)
        print('- height:/t', height)


class Warrior(Human):

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    
