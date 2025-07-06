import math
import pytest

data=[
    ([1,2,3],'sum',6),
    ([2,3,4],'prod',24)]
@pytest.mark.parametrize("a,b,c",data)
def test_demo(a,b,c):
    if b=='sum':
        assert sum(a)==c
        print(f"sum of {a} is {c}")
    else:
        assert math.prod(a)==c
        print(f"product of {a} is {c}")
    
    