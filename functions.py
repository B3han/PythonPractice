def find_total(expenses):
    '''
    This function takes expenses list as an input
    and return a total sum of that list
    :param expenses: list of input expenses
    :return: total expense
    '''
    total = 0
    for expense in expenses:
        total += expense
    return total

print(help(find_total))

def find_cylinder_volume(radius, height=7):
    print("radius:", radius)
    print("height:", height)
    volume = 3.14*(radius**2)*height
    return volume


r = 5
h = 10

print(find_cylinder_volume(radius=r, height=h))
