#Chain_of_responsibilities
class ConstructionProcess:
    def __init__(self, successor=None):
        self.successor = successor

    def construct(self, item):
        if self.successor:
            return self.successor.construct(item)
        return None

class SitePreparation(ConstructionProcess):
    def construct(self, item):
        if item == 'clear_site':
            print("SitePreparation: Clearing the site")
            return True
        elif self.successor:
            return self.successor.construct(item)
        return False
    
class Foundation(ConstructionProcess):
    def construct(self, item):
        if item == 'lay_foundation':
            print("Foundation: Laying the foundation")
            return True
        elif self.successor:
            return self.successor.construct(item)
        return False


class Building(ConstructionProcess):
    def construct(self, item):
        if item == 'construct_building':
            print("Building: Constructing the building")
            return True
        elif self.successor:
            return self.successor.construct(item)
        return False

class Roofing(ConstructionProcess):
    def construct(self, item):
        if item == 'add_roof':
            print("Roofing: Adding the roof")
            return True
        elif self.successor:
            return self.successor.construct(item)
        return False

class InteriorDesign(ConstructionProcess):
    def construct(self, item):
        if item == 'design_interior':
            print("InteriorDesign: Designing the interior")
            return True
        elif self.successor:
            return self.successor.construct(item)
        return False

class FinalTouch(ConstructionProcess):
    def construct(self, item):
        if item == 'add_final_touch':
            print("FinalTouch: Adding final touches")
            return True
        elif self.successor:
            return self.successor.construct(item)
        return False
