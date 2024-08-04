from sim.industry.trait import Trait

class GoodTemplate():
    '''Template class of good, stores data that is the same for any instance of the good'''

    def __init__(self, id:str, name:str, volume:float, packing_density:float, phase:int=0, inate_traits:list[Trait]=[]):
        self._id = id
        '''id of good'''
        self._name = name
        '''display name of good'''
        self._volume = volume
        '''volume of good, used for packed volume and mass calculations'''
        self._packing_density = packing_density
        '''best possible packing density of good, 1.0=good packs as densily as possible, 0.5=good can only fill 50% of volume required to pack it, 0.2=good can only fill 20% of volume required to pack it.'''
        self._phase = phase
        '''phase of good, 0=solid, 1=liquid, 2=gas'''
        self._inate_traits = inate_traits
        '''inate traits of good'''
    
    def get_traits(self) -> list[Trait]:
        return self._inate_traits
    
    def to_dict(self) -> dict:
        return {"ID":self._id, "Name":self._name, "Volume":self._volume, "PackingDensity":self._packing_density, "Phase":self._phase, "InateTraits":self._inate_traits}
    
    @classmethod
    def from_dict(cls, dict):
        return cls(id=dict["ID"], name=dict["Name"], volume=dict["Volume"], packing_density=dict["PackingDensity"], phase=dict["Phase"], inate_traits=dict["InateTraits"])

class Good():
    '''Base class type of good. Contains information about the good including its Id and traits'''

    def __init__(self, id:str, traits:list[Trait]=[], quantity:int=0) -> None:
        self._id:str = id
        '''Id of the good in the dictionary of goods'''
        self._traits = traits
        '''Traits of the good'''
        self._meta_data = []
        '''Meta data of good, used for any extra data that needs to be added to the good, usually empty'''
        pass

    # Traits
    def add_traits(self, traits:list[Trait]) -> bool:
        for trait in traits:
            self.add_trait(trait)
        return True
    
    def add_trait(self, trait:Trait) -> bool:
        self._traits.append(trait)
        return True
    
    def get_traits(self) -> list[Trait]:
        traits = self._traits.copy()
        global sim_main
        traits.extend(sim_main.goods[self._id].get_traits())
        return traits