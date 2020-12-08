
def max_min_tick(num, tick):

    max, min = self.find_max_min(num)

    if (max - min) // tick > 4:
        max_temp = (max // tick + 1) * tick
        if abs(max - max_temp) < 0.2 * tick:
            max = (max // tick + 2) * tick
        else:
            max = max_temp

        min_temp = (min // tick) * tick
        if abs(min - min_temp) < 0.2 * tick:
            min = (min // tick - 1) * tick
        else:
            min = min_temp
    else:
        tick = 0.5*tick
        max_temp = (max // tick + 1) * tick
        if abs(max - max_temp) < 0.2 * tick:
            max = (max // tick + 2) * tick
        else:
            max = max_temp

        min_temp = (min // tick) * tick
        if abs(min - min_temp) < 0.2 * tick:
            min = (min // tick - 1) * tick
        else:
            min = min_temp

    return max, min, tick
