from operator import itemgetter

def search(sequence, expected, finder):
    for element in sequence:
        if finder(element) == expected:
            return element
    raise RuntimeError(f"Could not find an element with '{expected}'")


friends = [
    {'name': 'josué', 'age': 23},
    {'name': 'anna', 'age': 29},
    {'name': 'elisa', 'age': 33},
]


def get_friend_name(friend):
    return friend['name']


# res = search(friends, 'bruno', finder=get_friend_name)
# res = search(friends, 33, lambda friend: friend['age'])
res = search(friends, 'anna', itemgetter('name'))
print(res)
