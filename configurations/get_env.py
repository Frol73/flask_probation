import os

from dotenv import load_dotenv


class GetData:
    dotenv_path = os.path.dirname(__file__) + "/env"
    load_dotenv(dotenv_path)

    @staticmethod
    def gat_data(value: str) -> str:
        return os.environ[value]
