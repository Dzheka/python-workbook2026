from intro.shopping.shopping import result


def friends_of(pairs, name):
    result = []
    for i in pairs:
       for person_index in [0, 1]:
           if i[person_index] == name:
               if person_index:
                   result.append(i[0])
               else:
                   result.append(i[1])

    return sorted(result)

def suggestions(pairs, name):
    result = []
    frieds_of_name = friends_of(pairs, name)
    for i in frieds_of_name:
        for j in friends_of(pairs, i):
            







pairs = [
            ["Ali", "Sara"], ["Ali", "Bek"], ["Sara", "Nilu"],
            ["Bek", "Nilu"], ["Bek", "Timur"], ["Nilu", "Madina"],
        ]
print(friends_of(pairs, 'Ali'))
