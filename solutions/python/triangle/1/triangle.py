def equilateral(sides):
    # assert 0 not in sides, False
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b >= c and b + c >= a and a + c >= b:
        return a == b == c
    return False

def isosceles(sides):
    assert 0 not in sides
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if a + b >= c and b + c >= a and a + c >= b:
        return a == b != c or a != b == c or a == c != b or a == b == c
    return False

def scalene(sides):
    assert 0 not in sides
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if a + b >= c and b + c >= a and a + c >= b:
        return a != b != c and a != c != b
        return False
    return False
