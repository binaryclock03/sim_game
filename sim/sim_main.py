from sim.player.player import Player
from sim.industry.industry_sim import IndustrySim
from sim.industry.industry import Industry

class SimMain():
    players:list[Player]
    goods:dict
    recipes:dict

    def __init__(self):
        self.industry_sim = IndustrySim()
        self.players = [Player('binary')]
    
    def startup(self):
        industry = Industry(recipe = self.recipes["millGrain"])
        self.industry_sim.add_industry(industry)

    def tick(self):
        self.industry_sim.tick(self)