from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Student, Discount, Category, Notification
from .serializer import StudentSerializer, DiscountSerializer, CategorySerializer, NotificationSerializer
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
        serializer = StudentSerializer(self.user)
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
        serializer.save()
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
    def bookmarks(self, request):
        """
        Bookmarks Custom Action

        Fetches all bookmarks associated with a specific student instance.
        
        Parameters:
            request (HttpRequest): The incoming HTTP request.
            
        Returns:
            HttpResponse: JSON response containing the student's bookmarks.
        """
        student = self.get_object()
        bookmarks = student.bookmarks.all()
        serializer = DiscountSerializer(bookmarks, many=True)
        return Response(serializer.data)

class DiscountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Discount ViewSet
    
    Exposes read-only endpoints for fetching discount information. 
    Students can only read the data; only superusers have the power to create or modify discounts.
    
    Attributes:
        serializer_class (class): Specifies the serializer to use, in this case, DiscountSerializer.
        permission_classes (list): A list of permission classes that the view uses to determine
        if a user has permission for an action. Utilizes the built-in ReadOnly permission to only allow 
        read actions for authenticated users.
    """
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Category ViewSet
    
    Exposes read-only endpoints for fetching category information.
    Also includes a custom action to fetch all discounts in a particular category.
    
    Attributes:
        ... (Same as before)
    """
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['GET'])
    def discounts_in_category(self, request, pk=None):
        """
        Discounts In Category Custom Action

        Fetches all discounts associated with a specific category instance.
        
        Parameters:
            request (HttpRequest): The incoming HTTP request.
            pk (int, optional): The primary key of the category. Defaults to None.

        Returns:
            HttpResponse: JSON response containing the discounts in the category.
        """
        category = self.get_object()
        discounts = category.get_discounts_in_category()
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)

class NotificationViewSet(viewsets.ModelViewSet):
    """
    Notification ViewSet
    
    Handles CRUD operations for Notifications and exposes additional custom actions.
    Limits data exposure by only returning the Notifications intended for the authenticated user.
    
    Attributes:
        serializer_class (class): Specifies the serializer to use, in this case, NotificationSerializer.
        permission_classes (list): A list of permission classes that the view uses to determine 
        if a user has permission for an action. Utilizes 
        IsAuthenticatedOrReadOnly to only allow authenticated 
        users to make changes.
    """
    serializer_class = NotificationSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        """
        Override the default query set to limit data exposure.

        Returns:
            QuerySet: A QuerySet containing only the authenticated user's Notifications.
        """
        return Notification.objects.filter(student=self.request.user.id)

    @action(detail=True, methods=['POST'])
    def mark_as_read(self, request, pk=None):
        """
        Mark Notification as Read Custom Action

        Marks a specific notification as read.
        
        Parameters:
            request (HttpRequest): The incoming HTTP request.
            pk (int, optional): The primary key of the notification. Defaults to None.

        Returns:
            HttpResponse: JSON response indicating the operation's success.
        """
        notification = self.get_object()
        notification.mark_as_read()
        return Response({'message': 'Notification marked as read.'})