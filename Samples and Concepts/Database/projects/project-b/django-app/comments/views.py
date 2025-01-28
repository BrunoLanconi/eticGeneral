import logging
from django.http import JsonResponse
from mongo.models import Comments
from mongo.mongo import Mongo
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

mongo = Mongo()
logging.basicConfig(level=10)


def get_comments(request: Request, phrase_id: int):
    comments = mongo.get_comments(phrase_id=phrase_id)

    if not comments:
        return JsonResponse(
            data={"error": "Comments not found"}, status=HTTP_404_NOT_FOUND
        )

    serializer = Comments(root=comments)

    return JsonResponse(data={"comments": serializer.model_dump()}, status=HTTP_200_OK)
