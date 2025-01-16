IDU config library is dedicated for automatic environment variables loading 
from .env files and changing.

Be advised that your .env file should be named as `.env.{TYPE}`
where `{TYPE}` is value of `APP_ENV` environment variable.

This allows you to have multiple .env files for different scenarios
and swapping between them easily on your code launch.
```python
from iduconfig import Config

# This line automatically loads variables from your .env file
config = Config()

# Now you can access them through .get(...) method
env_value = config.get("KEY")

# Or you can set new value for environment variable (even if doesn't exist)
config.set("KEY", "NEW_VALUE")
```