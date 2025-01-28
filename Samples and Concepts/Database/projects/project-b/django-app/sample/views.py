from django.http import JsonResponse
from mongo.models import Samples
from mongo.mongo import Mongo
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

mongo = Mongo()


class SampleView(APIView):
    def get(self, _: Request, name: str):
        sample = mongo.get_sample(name=name)

        if not sample:
            return JsonResponse(
                data={"error": "Sample not found"}, status=HTTP_404_NOT_FOUND
            )

        return JsonResponse(data=sample.model_dump(), status=HTTP_200_OK)


class SamplesView(APIView):
    def get(self, _: Request):
        samples = mongo.get_samples()
        serializer = Samples(root=samples)

        return JsonResponse(
            data={"samples": serializer.model_dump()}, status=HTTP_200_OK
        )
