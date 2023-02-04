def feedDog(hunger_level, biscuit_size):
    hunger_level = sorted(hunger_level)
    biscuit_size = sorted(biscuit_size)

    dogs_fed = 0
    biscuit_pointer = 0
    hunger_pointer = 0

    biscuit_n = len(biscuit_size)
    hunger_n = len(hunger_level)

    while biscuit_pointer < biscuit_n and hunger_pointer < hunger_n:
        if biscuit_size[biscuit_pointer] >= hunger_level[hunger_pointer]:
            dogs_fed += 1
            biscuit_pointer += 1
            hunger_pointer += 1
        else:
            hunger_pointer += 1
    
    return dogs_fed


