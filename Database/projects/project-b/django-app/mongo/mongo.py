from urllib.parse import quote_plus
from django.conf import settings
from mongo.models import Comment, Sample
from pymongo import MongoClient


class Mongo:
    def __init__(
        self,
        database: str = settings.MONGO_DB,
        host: str = settings.MONGO_HOST,
        password: str = settings.MONGO_PASSWORD,
        port: int = settings.MONGO_PORT,
        user: str = settings.MONGO_USERNAME,
    ):
        self.default_database = database
        self.uri = "mongodb://%s:%s@%s:%i/" % (
            quote_plus(user),
            quote_plus(password),
            host,
            port,
        )

    def get_samples(self) -> list[Sample]:
        with MongoClient(self.uri) as client:
            db = client.get_database(self.default_database)
            collection = db.get_collection("samples")
            samples = collection.find()

            return [Sample(**sample) for sample in samples]

    def get_sample(self, name: str) -> Sample | None:
        with MongoClient(self.uri) as client:
            db = client.get_database(self.default_database)
            collection = db.get_collection("samples")
            sample = collection.find_one({"name": name})

            if not sample:
                return None

            return Sample(**sample)

    def get_comments(self, phrase_id: int) -> list[Comment]:
        with MongoClient(self.uri) as client:
            db = client.get_database(self.default_database)
            collection = db.get_collection("comments")
            comments = collection.find({"phrase_id": phrase_id})

            return [Comment(**comment) for comment in comments]