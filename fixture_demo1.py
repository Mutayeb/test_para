# Parts of fixture: Setup and Teardown:
import pytest
weekdays1=['mon','tue', 'wed']
weekdays2=['fri','sat',' sun']

@pytest.fixture()
def setup01():
    wk1=weekdays1.copy()
    wk1.append('thu')
    yield wk1

    #till above line whatever we write is the yield part of the fixture and is run before the test case execution begins,here we performa ll actions needed
    # for example establsihing db connection, setting up web driver, etc.
    # we can also use yield to return a value from the fixture function.
    # the value returned by the fixture function can be used in the test case function.
    #  whatever we write after the yield is the teardown part of the fixture.
    #the teardown part of the fixture is run after the test case is run.which can be verified by the print statement below is printed
    # after the test case is passed
    print("\n ...... After yield in setup01 fixture....... \n")
    wk1.pop()


def test_exday(setup01):
    setup01.extend(weekdays2)
    print(setup01)

    assert setup01==['mon', 'tue', 'wed', 'thu', 'fri', 'sat', ' sun']
    assert setup01[0] == 'mon'
    assert setup01[1] == 'tue'
