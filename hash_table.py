"""Implement a hash table using only arrays."""


table = [None]*5


lst = ["hi", "amber", "yellow", "stone"]
pairs = {"hi": "a",  "amber": "b", "yellow":"c", "stone":"d"}

def make_hash_table(pairs):
    """add values to the hash table"""

    for item in pairs:
        code = hash(item)

        arr_val = code % len(table)
        
        if table[arr_val] is None:
            table[arr_val] = [[item, pairs[item]]]
        else:
            table[arr_val].append([item, pairs[item]])

    return table


def look_up(key):
    """return the key's index in the hash table."""

    return hash(key) % len(table)



if __name__ == '__main__':

    print(make_hash_table(pairs))

