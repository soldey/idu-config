import os
from pathlib import Path

from dotenv import load_dotenv


class Config:
    def __init__(self):
        self._validate()
        done = load_dotenv(Path().absolute() / f".env.{os.getenv('APP_ENV')}")
        if not done:
            raise RuntimeError("ENV_NOT_FOUND")

    @staticmethod
    def get(key: str) -> str:
        """Get environment variable.

        Args:
            key (str): name of variable.
        Returns:
            str: value of environment variable.
        Raises:
            ValueError: raised if environment variable does not exist.
        """

        tmp = os.getenv(key)
        if tmp:
            return tmp
        raise ValueError(f"No such env: {key}")

    @staticmethod
    def set(key: str, val: str) -> None:
        """Set value for environment variable.

        Args:
            key (str): name of environment variable.
            val (str): new value for environment variable.
        """

        os.environ[key] = val
        return

    @staticmethod
    def _validate():
        if not os.getenv("APP_ENV"):
            raise ValueError(f"APP_ENV variable is not present")

        try:
            with open(Path().absolute() / f".env.{os.getenv('APP_ENV')}"):
                pass
        except Exception as e:
            raise FileNotFoundError(f"Couldn't find file with .env.{os.getenv('APP_ENV')} name")
