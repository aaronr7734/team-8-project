from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import *
from .serializer import *
from .permissions import IsOwnerOrReadOnly

class CustomLoginView(LoginView):
    """
    Custom Login View
    
    Handles user authentication and token generation.
    """
    def get_response(self):
        """
        Customizes the login response to include the token and user details.
        """
        serializer = self.get_serializer(self.user)
        
        # Create or fetch the token
        token, created = Token.objects.get_or_create(user=self.user)
        
        # Prepare the response data
        data = {
            'token': token.key,
            'user': serializer.data
        }
        
        return Response(data)

class CustomRegisterSerializer(RegisterSerializer):
    """
    Custom serializer for user registration.
    """
    class Meta(RegisterSerializer.Meta):
        fields = ['first_name', 'last_name', 'email', 'password']

@api_view(['POST'])
def register_view(request):
    """
    Register a new user.

    Parameters:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: JSON response containing the new user's details.
    """
    serializer = CustomRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({'message': 'User registered successfully!', 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentViewSet(viewsets.ModelViewSet):
    """
    Student ViewSet
    
    Handles CRUD operations for the authenticated Student's data and exposes additional custom actions.
    Limits data exposure by only returning the Student instance for the authenticated user.
    
    Attributes:
        serializer_class (class): Specifies the serializer to use, in this case, StudentSerializer.
        permission_classes (list): A list of permission classes that the view uses to determine 
        if a user has permission for an action. Utilizes 
        IsAuthenticatedOrReadOnly to only allow authenticated 
        users to make changes.
    """
    serializer_class = StudentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def get_queryset(self):
        """
        Override the default query set to limit data exposure.

        Returns:
            QuerySet: A QuerySet containing only the authenticated user's Student instance.
        """
        return Student.objects.filter(id=self.request.user.id)

    @action(detail=True, methods=['GET'])
    def bookmarks(self, request, pk=None):
        """
        Bookmarks Custom Action

        Fetches all bookmarks associated with a specific student instance.
        
        Parameters:
            request (HttpRequest): The incoming HTTP request.
            pk (int, optional): The primary key of the student. Defaults to None.

        Returns:
            HttpResponse: JSON response containing the student's bookmarks.
        """
        student = self.get_object()
        bookmarks = student.bookmarks.all()
        serializer = DiscountSerializer(bookmarks, many=True)
        return Response(serializer.data)
