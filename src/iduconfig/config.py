import os
from pathlib import Path

from dotenv import load_dotenv


class Config:
    def __init__(self):
        done = load_dotenv(Path().absolute() / f".env.{os.getenv('APP_ENV')}")
        if not done:
            raise RuntimeError("ENV_NOT_FOUND")

    @staticmethod
    def get(key: str) -> str:
        tmp = os.getenv(key)
        print(tmp)
        if tmp:
            return tmp
        raise ValueError(f"No such env: {key}")

    @staticmethod
    def set(key: str, val: str) -> None:
        os.environ[key] = val
        return
