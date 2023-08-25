# You have a hundred cats
# One day, you decided to arrange all your cats in a giant circle. Initially, none of your cats has a hat on. You walk
# around the circle a hundred times, always starting with the first cat. Each time you stop at a cat, you check if it
# has a hat on. If it doesn't, then you put a hat on it. If it does, then you take the hat off.

def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    # We want to walk around the circle 100 times
    for num in range(1, 100 + 1):
        # Each time we walk around, we visit 100 cats
        for cat in range(1, 100 + 1):
            # Determine whether to visit the cat
            # Use modulo operator to visit every 2nd, 3rd, 4th,... etc.
            if cat % num == 0:
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True
    # Add all numbers of each cat with a hat to a list
    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)

    return cats_with_hats_on

# Cats contains whether each cat already has a hat on, by default all are set to false since none have been visited
cats = [False] * ( 100 + 1 )
print(get_cats_with_hats(cats))