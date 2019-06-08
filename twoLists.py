def eltToElt(list1, list2):
    """A list associating to each element elt of list1, either an element of list 2, or None.

    If elt is in list2, it is associated to itself.  Each element of
    list1 is associated to a distinct element of list2. If they are
    more element in list2 than in list1, then the last elements of
    list1 are associated to None.

    """
    set1 = set(list1)
    set2 = set(list2)
    used2 = set()
    mapping = []
    usableValue = [value for value in list2 if value not in set1]
    nbUsableValues = len(usableValue)
    usedValues = 0
    for key in list1:
        if key in set2:
            value = key
        elif usedValues < nbUsableValues:
            value = usableValue[usedValues]
            usedValues +=1
        else:
            value = None
        mapping.append((key,value))
    print(f"eltToElt({list1},{list2}) = {mapping}")
    return mapping
    
    
def eltToPos(list1, list2):
    """Similar to eltToElt, but also associate the position of the value in list2. Or the length of list2 its not a value."""
    reverse = dict()
    l = len(list2)
    for pos, elt in enumerate(list2):
        reverse[elt] = pos
    mapping = [(reverse.get(value, l), key) for key, value in  eltToElt(list1, list2)]
    print(f"eltToElt({list1},{list2}) = {mapping}")
    return mapping
    
