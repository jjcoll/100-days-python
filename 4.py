# # must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# # must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

def cakes(recipe, available):
    arr = []
    for i in recipe:
        # check if ingredient is available
        if i in available:
        # create a list with amount of each that one can make
            arr.append(int(available.get(i) / recipe.get(i)))
        else:
            return 0
    return min(arr)


# One liner