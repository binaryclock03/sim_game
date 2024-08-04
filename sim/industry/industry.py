from sim.industry.recipe import Recipe

class Industry():
    def __init__(self, recipe:Recipe, owner=None):
        self._recipe:Recipe = recipe
        self._enabled:bool = True
        self._owner = owner

    def request_inputs(self) -> dict:
        return self._recipe.get_inputs()

    def provide_inputs(self, inputs:dict):
        if self._enabled:
            pass

    def proccess_products(self):
        if self._enabled:
            pass

    def dump_products(self):
        if self._enabled:
            pass