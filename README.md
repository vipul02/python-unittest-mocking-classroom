# python-unittest-mocking-classroom

Note it's preferred to use Git bash terminal when on Windows. You can download it from [here](https://git-scm.com/downloads). 

Also, Python3.7 should be installed and added to PATH.
 
    $ python --version
    Python 3.7.3


### Goal
* Fork the project.
* Clone the repo.
* Create a child(feature) branch from master branch.
* In the child(feature) branch, implement missing functions and add new tests using mock to make the unit tests pass (run tests locally).
* Push the child(feature) branch from local to the remote.
* Share the link to your repo.

### How to run tests locally
Before running tests locally make sure, you have forked the project to create your own copy of the repo. Then clone the repo into your local machine.

Cd into your local repo
     
    $ cd python-unittest-mocking-classroom
    User@DESKTOP- MINGW64 /f/Learnings/TDD/python-unittest-mocking-classroom (master)
    
As can be seen above, currently the local repo points to the `master` branch. Create a chile branch with name `feature/add-tests`

    $ git checkout -b feature/add-tests
    Switched to a new branch 'feature/add-tests'
    
Now that you are checked in to child branch, you can start working on code.

     
Make sure you are in the root directory of the project

    $ ls
    README.md  src  tests
    
Then create a virtual environment for the project.

On Linux

    $ virtualenv -p python venv
    $ . venv/bin/activate

On Windows
Powershell
  
    > virtualenv -p python venv
    > .\venv\Scripts\activate

Git Bash

    $ virtualenv -p python venv
    $ . venv/Scripts/activate

    
Run the tests

    $ python -m unittest
    
You should see the following failing output

    ----------------------------------------------------------------------
    Ran 2 tests in 0.002s

    OK
    
Reference files (src/calculator.py and tests/test_calculator.py) have been provided to understand how mocking works. And that's why the above 2 tests are passing.

Another skeleton file (src/db_helper.py) has been provided. You need to implement the two methods to calculate min and max salary. You can create a sample table in localhost MySQL server, insert a few test records and can refer the same in the code. 

After implementation, run

    $ python src/db_helper.py
    
The above command should print the min and max salary to the console as can been seen in the code.

Create a test file `test_db_helper.py` inside tests directory. Add a test method `test_max_salary_is_greater_than_min_salary` to assert that max salary is greater than min salary. Note you need to mock the two methods here and return a custom output so that the tests don't make actual DB calls. You can use self.assertGreater() for assertion.

Run the tests

    $ python -m unittest
    
You should now see one added test to the output and all tests must pass.

    ----------------------------------------------------------------------
    Ran 3 tests in 0.002s

    OK
     
Commit all the code changes and push the feature branch to the remote.