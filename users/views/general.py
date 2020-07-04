""" User endpoints. """

from cerberus import Validator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from ..serializers import UserSerializer
from ..models.user import User
from ..helpers import paginate_content


class UserApi(APIView):
    """ User http verbs """

    @paginate_content()
    # pylint: disable=no-member
    def get(self, request):
        """ """
        filters = []
        if "start_date" in request.GET:
            filters.append(Q(created_at__lte=request.GET.get("start_date")))
        if "end_date" in request.GET:
            filters.append(Q(created_at__gte=request.GET.get("end_date")))

        data = User.objects.filter(*filters)
        return Response(
            {
                "count": data.count(),
                "data": UserSerializer(
                    data[self.pagination_start: self.pagination_end + 1],
                    many=True).data,
            }, status=status.HTTP_200_OK)

    def post(self, request):
        """ Creates a new user.

        Parameters:
            request (dict): Contains http transaction information.

        Returns:
            Response (serializer,status): The serialization and a status code.

        """

        validator = Validator({
            "email": {"required": True, "type": "string", "empty": False},
            "first_name": {"required": True, "type": "string", "empty": False},
            "last_name": {"required": True, "type": "string", "empty": False},
            "password": {"required": True, "type": "string", "empty": False},
            "profession": {"required": True, "type": "string", "empty": False},
        })
        if not validator.validate(request.data):
            return Response({
                "code": "Invalid body",
                "detailed": "There are errors in your request",
                "data": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "code": "Invalid body",
                "detailed": "There was an error creating user",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer.create(validated_data=request.data)
        return Response(status=status.HTTP_201_CREATED)
