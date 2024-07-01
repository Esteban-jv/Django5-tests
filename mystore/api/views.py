from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)
        # Check password
        pwd_valid = check_password(password, user.password)
        if not pwd_valid:
            return Response("User or password invalid")
        # Create or change token
        token,_ = Token.objects.get_or_create(user=user)
        # print(token)

        return Response(token.key)
    except User.DoesNotExist:
        return Response("User is not valid")
