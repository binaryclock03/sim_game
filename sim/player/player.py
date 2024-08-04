from sim.industry.good import Good

class Player():
    def __init__(self, player_name:str="default_name"):
        self._player_name = player_name
        self._inventory = dict[Good:int]()
        #self._character
    
    def add_good_to_inventory(self, good:Good, quantity:int) -> int:
        if quantity > 0:
            if good in self._inventory.keys():
                self._inventory[good] += quantity
            else:
                self._inventory[good] = quantity
            return quantity
        return 0
    
    def remove_good_from_inventory(self, good:Good, quantity:int) -> int:
        if quantity < 0:
            if self.can_remove_good_from_inventory(good, quantity):
                if not self._inventory[good] - quantity == 0:
                    self._inventory[good] -= quantity
                else:
                    self._inventory.pop(good)
                return quantity
        return 0
        
    def can_remove_good_from_inventory(self, good:Good, quantity:int) -> bool:
        if good in self._inventory.keys():
            if self._inventory[good] >= quantity:
                return True
        return False