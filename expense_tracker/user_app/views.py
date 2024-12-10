


from .models import CustomUser
from .serailizers import CustomSerailizer


from rest_framework.generics import ListCreateAPIView



class CustomUserView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerailizer









    

