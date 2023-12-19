# tracker/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def data_all(request):
    if request.method == 'GET':
        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def data_all(request):
    if request.method == 'GET':
        snippets = Task.objects.all()
        serializer = TaskSerializer(snippets, many=True)
        return Response(serializer.data)

    
class ApiRootView(APIView):
    def get(self, request, format=None):
        data = {
            "tasks": reverse("task-list", request=request, format=format),
            "login": reverse("login", request=request, format=format),
            "signup": reverse("signup", request=request, format=format),
            "logout": reverse("logout", request=request, format=format),
            "data_all" : reverse("data_all",request=request,format=format)
        }
        return Response(data, status=status.HTTP_200_OK)
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 
    def list(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return super().list(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Authentication required for this action'}, status=status.HTTP_401_UNAUTHORIZED)


class SignupView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username is already taken'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return JsonResponse({'success': 'User registered successfully'}, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'success': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['POST'])
def logout_view(request, format=None):
    try:
        logout(request)
        return Response({'success': 'Logout successful'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

