#another of calling a fixture by marking/markers  it with @pytest.mark.usefixtures
# fixture function will be called in this line that we write before wrting our test csae:
# @pytest.mark.usefixtures("setup_list")
#drawback : return values of the fixture function cannot be used in the test case function.


import pytest
@pytest.fixture()  # This function is fixture.
def setup_list():       # This function is fixture.
    # This function will be run before each test
    print("\n ...... indside fixture....... \n")
    city= ["New York", "New Jersey", "California", "Texas"]
    return city


#2nd method of using fixture: in the same file and use it in a test case by using marker:
#this method of using fixture is not recommended as we cannot use the return value of the fixture in the test case:

@pytest.mark.usefixtures("setup_list")  # This function uses fixture.
                                    # ensures the fixture is run, but does NOT inject it as a variable into your test function.
@pytest.mark.xfail(reason="This test is expected to fail as the tes case cannot access fixture's return value")
def test_get2():
    print("\n ...... indside test_get1....... \n")
    assert setup_list()[::-2]==["Texas", "New Jersey"]       #this line returns error because setup_list is not defined in this function.
    assert 1==1