from pymongo import MongoClient, uri_parser
from pymongo.database import Database

from gridfs import GridFS


class WrappedMongoClient(MongoClient):
    def __init__(self, mongo_uri: str = None, *args, **kwargs) -> None:
        self.client: MongoClient | None = None
        self.db: Database | None = None
        self.gridfs: GridFS | None = None

        if mongo_uri is not None:
            self.init_db(mongo_uri, *args, **kwargs)

    def init_db(self, mongo_uri: str, *args, **kwargs) -> None:
        self.client = MongoClient(mongo_uri, *args, **kwargs)

        if (database := uri_parser.parse_uri(mongo_uri).get('database')):
            self.db = self.client[database]
            self.gridfs = GridFS(database=self.client[database], collection='files')
