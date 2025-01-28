# [Testing](https://docs.python.org/3/library/unittest.html)

Python has a built-in module called `unittest` that allows you to write test cases for your code. It is a good practice to write tests for your code to ensure that it works as expected.

### Example
```python
import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

The code above defines a function `add` that adds two numbers and a test case `TestAdd` that tests the `add` function. The `assertEqual` method is used to check if the result of the function is equal to the expected result.

To run the test cases, you can execute the script directly or use the following command:

```bash
python -m unittest test_add.py
```

The output will show if the test cases passed or failed.

---

## Naming Conventions

The `unittest` module provides a way to organize test cases in test files and directories. You can create test files with the prefix `test_` and test directories with the prefix `test_` to run all test cases in the files or directories.

### Example
```bash
.
...
└── tests
    └── test_add.py
```

You can create test classes with the prefix `Test` to run all test cases in the classes.

### Example
```python
class TestAdd(unittest.TestCase):
    """
    A test case for the add function.

    Methods:
        - setUp: Set up the test case.
        - tearDown: Tear down the test case.
        - test_add: Test the add function.
    """

    ...

    def test_add(self):
        """
        Test the add function.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
```

---

## [Test Fixtures](https://docs.python.org/3/library/unittest.html#class-and-module-fixtures)

Test fixtures are used to set up and tear down resources for test cases. You can use the `setUp` and `tearDown` methods to prepare and clean up resources before and after each test case.

### Example
```python
import unittest

from src.modules.add import add


class TestAdd(unittest.TestCase):
    """
    A test case for the add function.

    Methods:
        - setUp: Set up the test case.
        - tearDown: Tear down the test case.
        - test_add: Test the add function.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        print("Setting up test case...")

    def tearDown(self):
        """
        Tear down the test case.
        """
        print("Tearing down test case...")

    def test_add(self):
        """
        Test the add function.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
```

The `setUp` method is called before each test case, and the `tearDown` method is called after each test case. You can use these methods to set up and tear down resources for the test cases. If you need to set up and tear down resources for the entire test case, you can use the `setUpClass` and `tearDownClass` methods.

### Example
```python
import unittest

from src.modules.add import add


class TestAdd(unittest.TestCase):
    """
    A test case for the add function.

    Methods:
        - setUpClass: Set up the test case.
        - tearDownClass: Tear down the test case.
        - test_add: Test the add function.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test case.
        """
        print("Setting up test case...")

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the test case.
        """
        print("Tearing down test case...")

    def test_add(self):
        """
        Test the add function.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
```

While the `setUp` and `tearDown` methods are called before and after each test case, the `setUpClass` and `tearDownClass` methods are called before and after the test case class.

---

## [Decorators](https://docs.python.org/3/library/unittest.html#organizing-test-code)

The `unittest` module provides decorators to organize test code. You can use the `@unittest.skip` decorator to skip test cases, the `@unittest.skipIf` decorator to skip test cases based on a condition, and the `@unittest.skipUnless` decorator to skip test cases unless a condition is met.

### Example
```python
import unittest

from src.modules.add import add


class TestAdd(unittest.TestCase):
    """
    A test case for the add function.

    Methods:
        - test_add: Test the add function.
    """

    @unittest.skip("Skip this test case.")
    def test_add(self):
        """
        Test the add function.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)

    @unittest.skipIf(True, "Skip this test case if True.")
    def test_add(self):
        """
        Test the add function.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)

    @unittest.skipUnless(False, "Skip this test case unless False.")
    def test_add(self):
        """
        Test the add function.
        """
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
```

---

## [Exceptions](https://docs.python.org/3/library/unittest.html#assert-methods)

The `unittest` module provides assert methods to check if an exception is raised in a test case. For instance, you can use the `assertRaises` method to check if an exception is raised and the `assertRaisesRegex` method to check if an exception is raised with a specific message.

### Example
```python
...
from unittest.mock import Mock, patch

...

class TestAdd(unittest.TestCase):
    ...

    def test_add_expected_failure(self):
        """
        Test the add function with an expected failure.
        """
        with self.assertRaises(TypeError):
            add("1", 2)
            
    def test_add_expected_failure_with_message(self):
        """
        Test the add function with an expected failure and message.
        """
        with self.assertRaisesRegex(TypeError, "can only concatenate str"):
            add("1", 2)

...
```

---

## [Command Line Interface](https://docs.python.org/3/library/unittest.html#command-line-interface)

The `unittest` module provides a command-line interface to run test cases. You can use the `-v` option to show verbose output, the `-q` option to show quiet output, and the `-f` option to stop the test run on the first failure.

### Example
```bash
python -m unittest -v test_add.py
```

The `unittest` module provides lots of flags to customize the test run. Below are some of the flags:

- `-v`, `--verbose`: Verbose output.
- `-q`, `--quiet`: Quiet output.
- `-f`, `--failfast`: Stop the test run on the first failure.
- `-c`, `--catch`: Catch control-C and display results so far.
- `-b`, `--buffer`: Buffer stdout and stderr during test runs.
- `-k`, `--keyword`: Only run tests which match the given substring.

---

## [Mocking](https://docs.python.org/3/library/unittest.mock.html)

The `unittest.mock` module provides a way to mock objects for testing. You can use the `patch` function to replace objects with mock objects.

### Example
```python
...
from unittest.mock import Mock, patch

...

class TestAdd(unittest.TestCase):
    ...

    @patch("src.modules.add", return_value=3)
    def test_mock_add_with_patch(self, mock_add: Mock):
        """
        Test the add function with a mock and patch.
        """
        self.assertEqual(mock_add(), 3)
        self.assertEqual(mock_add.call_count, 1)

...
```

The `patch` function is used to replace the `add` function with a mock object that returns `3`. The `call_count` attribute is used to count the number of calls to the mock object. Note that the `patch` decorator injects `mock_add` as an argument to the test method.

You may also reach the same result by declaring a `Mock` object within the test method.

### Example
```python
...
from unittest.mock import Mock, patch

...

class TestAdd(unittest.TestCase):
    ...

    def test_mock_add(self):
        """
        Test the add function with a mock.
        """
        mock_add = Mock(return_value=3)

        self.assertEqual(mock_add(), 3)
        self.assertEqual(mock_add.call_count, 1)

...
```

