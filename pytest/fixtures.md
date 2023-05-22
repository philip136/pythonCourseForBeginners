# <span style="font-family:Helvetica; font-size:2em;">Fixtures</span>

## <span style="font-family:Helvetica; font-size:1em">Introduction to fixtures</span>
Pytest fixtures are functions that can be used to manage our apps states and dependencies. Most importantly, they can provide data for testing and a wide range of value types when explicitly called by our testing software.
We usually use fixtures if we want to create something and delete it after test.

Let's imagine the following situation: we have a database, and we need to perform certain operations with db.
The database will have the next implementation (it's an abstraction)
```python
from abc import ABC, abstractmethod

class DatabaseProvider(ABC):
    _connection = None
    
    @abstractmethod
    def connect(self):
        """This method is used to connect to the db.
        If we have a connection, we can perform any operations on the db.
        :return: Some kind of db interface.
        """
        pass
    
    @abstractmethod
    def close(self):
        """This method is used to disconnect from the db."""
        pass
    

class PostgresSQLProvider(DatabaseProvider):
    def connect(self):
        ...
        self._connection = pg_connection
    
    def close(self):
        ...
        self._connection.close()
```
Obviously, we won't be creating a new instance for every test because we'll have duplicate code. And we will waste time creating a new connection for db.
To solve this issue we have a fixture.

```python
import pytest


@pytest.fixture()
def database():
    pg_provider = PostgresSQLProvider()
    yield pg_provider.connect() 
    pg_provider.close()


def test_get_users(database):
    database.peform_query("SELECT email, password FROM USERS")
    ...
```
When our test starts executing it looks for the fixture we passed in as a parameter named `database`.
The `yield` keyword for a fixture works in the same way as `return`, but only after the `yield` keyword do we specify what should happen after the test has completed.
## Scopes for fixture
By default, any fixture has a `function` scope. This means that everything after `yield` will be executed after the test function or method has finished.
Also, fixture has the following scopes: `class`, `module`, `session`.

### Class scope
```python
import pytest


@pytest.fixture(scope="class")
def database(request):
    pg_provider = PostgresSQLProvider()
    pg_connection = pg_provider.connect()
    request.cls.pg_connection = pg_connection
    yield pg_connection
    pg_provider.close()
    

@pytest.mark.usefixtures("database")
class TestDatabaseQuery:
    def test_get_users(self):
        self.pg_connection.peform_query("SELECT email, password FROM USERS")
        ...
    
    def test_get_user_by_email(self):
        self.pg_connection.peform_query(f"SELECT email, password FROM USERS WHERE email='user1@gmail.com'")
        ...
```
In this case, the database will be closed after all tests from `TestDatabaseQuery` have been executed.
### Module scope
```python
import pytest


@pytest.fixture(scope="module")
def database():
    pg_provider = PostgresSQLProvider()
    yield pg_provider.connect()
    pg_provider.close()

    
def test_get_users(database):
    database.peform_query("SELECT email, password FROM USERS")
    ...

def test_get_user_by_email(database):
    database.peform_query(f"SELECT email, password FROM USERS WHERE email='user1@gmail.com'")

```
In this case, the database will be closed after all tests from `module` (file) have been executed.
### Session scope
```python
import pytest


@pytest.fixture(scope="session")
def database():
    pg_provider = PostgresSQLProvider()
    yield pg_provider.connect()
    pg_provider.close()

    
def test_get_users(database):
    database.peform_query("SELECT email, password FROM USERS")
    ... 
```
In this case, the database will be closed after all the tests that were run with pytest have run.
### Autouse fixtures
```python
import pytest
import time

@pytest.fixture(autouse = True, scope="module")
def fix_module():
    answer = 42
    print(f"Module setup {answer}")
    yield
    print(f"Module teardown {answer}")


@pytest.fixture(autouse = True, scope="function")
def fix_function():
    start = time.time()
    print(f"  Function setup {start}")
    yield
    print(f"  Function teardown {start}")


def test_one():
    print("    Test one")
    assert True
    print("    Test one - 2nd part")

def test_two():
    print("    Test two")
    assert False
    print("    Test two - 2nd part")

# --------- Result ---------
Module setup 42
  Function setup 1612427609.9726396
    Test one
    Test one - 2nd part
  Function teardown 1612427609.9726396
  Function setup 1612427609.9741583
    Test two
  Function teardown 1612427609.9741583
Module teardown 42
```
