# Challenge 04: Testing

Create a test suite for the given class using the `unittest` module.

## Materials

- Class: `AccountDispatcher`

```python
class AccountDispatcher:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.id] = account

    def get_account(self, account_id):
        if account_id not in self.accounts:
            raise ValueError(f"Account {account_id} not found")

        return self.accounts.get(account_id)

    def remove_account(self, account_id):
        if not account_id in self.accounts:
            raise ValueError(f"Account {account_id} not found")

        return self.accounts.pop(account_id, None)
```

## Challenge

- Test the expected exceptions for the `get_account` and `remove_account` methods.
- Create a test suite for the `AccountDispatcher` class.
- Test the `add_account`, `get_account`, and `remove_account` methods.
- Use the `unittest` module to create the test suite.

### Godlike Mode

- Create a Makefile to automate the process of running the tests.
- Use the `unittest.mock` module to mock the `Account.remove_account` method.

