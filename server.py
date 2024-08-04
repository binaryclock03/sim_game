def load_goods() -> dict:
    with open("data/goods.json") as f:
        data = f.read()
        import json
        data = json.loads(data)
        goods = {}
        from sim.industry.good import GoodTemplate
        for good_data in data:
            good = GoodTemplate.from_dict(good_data)
            goods.update({good._id:good})
        return goods

def load_recipies() -> dict:
    with open("data/recipes.json") as f:
        data = f.read()
        import json
        data = json.loads(data)
        from sim.industry.recipe import Recipe
        recipes = {}
        for recipe_data in data:
            recipe = Recipe.from_dict(recipe_data)
            recipes.update({recipe._id:recipe})
        return recipes

if __name__ == '__main__':
    from sim.sim_main import SimMain

    # setup sim
    print("Setting up simulation")
    sim_main = SimMain()
    
    # loading data
    print("Loading data")
    sim_main.goods = load_goods()
    sim_main.recipes = load_recipies()

    # startup sims
    sim_main.startup()

    # main loop
    print("Starting main loop")
    import time
    TICK_TIME:float = 1     # Tick time in seconds of main sim loop'''
    last_tick_time:float = 0      # Tracks last time execution time in seconds
    is_sim_running = True   # If true, main sim loop runs'''

    while is_sim_running:
        if (TICK_TIME - last_tick_time + 0.001) > 0:
            time.sleep(TICK_TIME - last_tick_time) # keep tick rate
        else:
            print("Simulation is running behind by: " + str(TICK_TIME - last_tick_time))

        tick_start_exec_time = time.time()
        print("Tick")

        # run the main sim tick... all game simulation happens in here
        sim_main.tick()

        last_tick_time = time.time() - tick_start_exec_time
    pass