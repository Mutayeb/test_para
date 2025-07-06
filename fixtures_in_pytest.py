# fixture in oytest: these are codes that are run before and after the actual test cases we intend to run,
# they are used to set up the environment for the test cases and also clean up after the test cases have run.
# fixtures are used to set up the environment for the test cases and also clean up after the test cases have run.   
# for example settign up db connections, setting up web drivers for webtesting in selenium, setting up test data, etc.
# we can use the fixtres in an individual file or in the entire directory
# we usuually define in the conftest.py file and we can use it in any test file in the directory or subdirectory.

# 2 ways o fusing fixtures: in the same file,in the multiple FileExistsError
#its not msndatory to use the fixtures in the same file, we can use it in multiple files.
#its not mandatory for  fixtures to return a value, we cn us eit to perform some action before the test case is run.