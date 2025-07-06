# Define Fixture in test-file an duse it in a test case in the same file as function argument

import pytest
@pytest.fixture()  # This function is fixture.
def setup_list():       # This function is fixture.
    # This function will be run before each test
    print("\n ...... indside fixture....... \n")
    city= ["New York", "New Jersey", "California", "Texas"]
    return city

#in above our fixture is returning a value but its not mandatory for  fixtures to return a value, we can use it to perform some action before the test case is run.

#A fixture function is called when we pass it as an argumenet to our test case
def rev_list(lst):       # This function is fixture.
    print("\n ...... indside rev_list....... \n")
    # city= ["New York", "New Jersey", "California", "Texas"]
    lst.reverse()
    return lst


def test_get(setup_list):      # This function uses fixture.
   print(setup_list[1:3])
   assert setup_list[1:3] == ["New Jersey", "California"]
   assert setup_list[0] == "New York"
   assert setup_list[1::2]== ["New Jersey", "Texas"]

def test_get1(setup_list):      # This function uses fixture.
    assert setup_list[::-2]==["Texas", "New Jersey"]
#  == ["Texas", "New Jersey"]

    assert rev_list(setup_list)== ["Texas", "California", "New Jersey", "New York"]
   
