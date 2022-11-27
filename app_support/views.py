from rest_framework import mixins
from rest_framework import generics
from .models import User, Country, State, City, Period, Product, Reparation, Departement
from .serializers import (UserSerializer, CountrySerializer, StateSerializer, CitySerializer,
                          PeriodSerializer, ProductSerializer, RepationSerializer, DepartementSerializer)
  

# view for country  
class CountryList(generics.ListCreateAPIView):
    
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
  
# view for state
class StateList(generics.ListCreateAPIView):
    
    queryset = State.objects.all()
    serializer_class = StateSerializer
 
# view City    
class CityList(generics.ListCreateAPIView):
    
    queryset = City.objects.all()
    serializer_class = CitySerializer

# view departement    
class DepartementList(generics.ListCreateAPIView):
    
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    
# view for User 
class UserList(generics.ListCreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

# View for Period    
class PeriodList(generics.ListCreateAPIView):
    
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

# view for product
class ProductList(generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# view for support person    
class ReparationList(generics.ListCreateAPIView):
    
    queryset = Reparation.objects.all()
    serializer_class = RepationSerializer
  
class RepartionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reparation.objects.all()
    serializer_class = RepationSerializer
