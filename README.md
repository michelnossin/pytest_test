This is some personal Pytest and docker play code. 
TODO : These tests are depending on their order.

# Best practices TDD and Unit Testing

Start simple:
Start with simplest test case and increase complexity (clean simple)
Complex cases will make you get stuck
It will also lead to bad design decisions

Use descriptive test name:
Reading is done 1000s times more than being written. Make it clear and readable
Unit test will be used as dcoumentation
Test suites should be named by the class or function being tested

Keep tests fast:
Fast feedback on changes
Keep output console minimum
Mockout slow collaborators using test doubles

Code coverage tools (eg pytest-gov):
Use these to prevent missing tests
goal = 100% for functions with real logic

Run tests multiple time and random (pytest-random-order plugin,  install with pip):
Prevents tests with dependencies
use --count 10 , and --random-order-bucket=none
Use configuration defaults like
``` 
# content of pytest.ini
# (or tox.ini or setup.cfg)
[pytest]
addopts = -rsxX -q
```
Or in spacemacs use pytest-cmd-flags variable
```
(defcustom pytest-cmd-flags "-x -s --count 10 --random-order"
  "These are the flags passed to the pytest runner.")
```

Static code anaylsis tools:
Pylint will find errors
Can verify you team standard or PEP8
Can generate UML diagrams based on code
