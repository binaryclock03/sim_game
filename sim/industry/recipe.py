class Recipe():
    def __init__(self, id:str, name:str, inputs:dict, outputs:dict, cycle_time:float):
        self._id:str            = id
        self._name:str          = name
        self._inputs:dict       = inputs
        self._outputs:dict      = outputs
        self._cycle_time:float  = cycle_time
    
    def get_name(self) -> str:
        return self._name

    def get_inputs(self) -> dict:
        return self._inputs
    
    def get_outputs(self) -> dict:
        return self._outputs
    
    def get_cycle_time(self) -> float:
        return self._cycle_time
    

    def to_dict(self) -> float:
        return {"ID":self._id, "Name":self._name, "Inputs":self._inputs, "Outputs":self._outputs, "CycleTime":self._cycle_time}
    
    @classmethod
    def from_dict(cls, dict):
        return cls(id=dict["ID"], name=dict["Name"], inputs=dict["Inputs"], outputs=dict["Outputs"], cycle_time=dict["CycleTime"])