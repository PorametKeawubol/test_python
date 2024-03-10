def Cat_and_Mouse(x, y, z):
    distance_cat_a = abs(z - x)
    distance_cat_b = abs(z - y)
    
    if distance_cat_a < distance_cat_b:
        return "Cat A"
    elif distance_cat_b < distance_cat_a:
        return "Cat B"
    else:
        return "Mouse C"