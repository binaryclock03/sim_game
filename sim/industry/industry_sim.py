#from sim.sim_main import SimMain
from sim.industry.industry import Industry

class IndustrySim():
    _industries:list[Industry]

    def __init__(self):
        self._industries = []
    
    def tick(self, main_sim):
        self._pre_tick(main_sim)
        self._tick(main_sim)
        self._post_tick(main_sim)

    def _pre_tick(self, main_sim):
        for industry in self._industries:
            inputs = industry.request_inputs()
            for input in inputs.keys():
                amount = inputs[input]
                global sim_main
                print(sim_main.players[0])

    def _tick(self, main_sim):
        pass

    def _post_tick(self, main_sim):
        pass

    def add_industry(self, industry:Industry):
        self._industries.append(industry)