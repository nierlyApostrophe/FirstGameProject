import unit_create as uc

class Team:

    def __init__(self, unit_cap: int=2):
        self.unit_cap = unit_cap
        self.unit_list_inst: list = [] # list of Unit instances
        self.unit_list: list = []      # list of strings for visual output
        self.unit_count: int = 0
        self.symbol: str = ""

    def add_unit(self, unit: uc.Unit) -> None:
        """
        Adds a unit to the team
        """
        if self.unit_count >= self.unit_cap:
            print("You've exceeded maximum unit count!")
        else:
            self.unit_count += 1
            if isinstance(unit, uc.Infantry):
                self.unit_list_inst.append(uc.Infantry())
            elif isinstance(unit, uc.Cavalry):
                self.unit_list_inst.append(uc.Cavalry())
            self.unit_list.append(unit.name)

    def health_check(self):
        for unit in self.unit_list_inst:
            if unit.is_dead():
                self.unit_list_inst.remove(unit)

if __name__ == "__main__":
    help(Team)
