import dataclasses
import dotenv
import os

dotenv.load_dotenv()


@dataclasses.dataclass
class DatabaseConfig():
    MONGODB_HOST: str = os.environ.get('MONGODB_HOST', '127.0.0.1')
    MONGODB_USER: str = os.environ.get('MONGODB_USER', 'admin')
    MONGODB_PASS: str = os.environ.get('MONGODB_PASS', 'admin')
    MONGODB_NAME: str = os.environ.get('MONGODB_NAME', 'test')
    MONGODB_URL: str = f'mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_HOST}/{MONGODB_NAME}?retryWrites=true&w=majority&connectTimeoutMS=5000&serverSelectionTimeoutMS=7000'


database_config = DatabaseConfig()
