# You have a hundred cats
# One day, you decided to arrange all your cats in a giant circle. Initially, none of your cats has a hat on. You walk
# around the circle a hundred times, always starting with the first cat. Each time you stop at a cat, you check if it
# has a hat on. If it doesn't, then you put a hat on it. If it does, then you take the hat off.

def get_cats_with_hats(array_of_cats):
    cats_with_hats_on = []
    for num in range(1, 100 + 1):
        for cat in range(1, 100 + 1):
            if cat % num == 0:
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True

    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)

    return cats_with_hats_on

cats = [False] * ( 100 + 1 )
print(get_cats_with_hats(cats))