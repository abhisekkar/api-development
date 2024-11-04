from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User,Product,Order,Category,Review
from .serializers import UserSerializer,ProductSerializer,OrderSerializer,CategorySerializer,ReviewSerializer

#create User
class CreatUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#Get User by id
class GetUser(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer=UserSerializer(user)
        return Response(serializer.data)
#Create Product
class CreateProduct(APIView):
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#list Products
class ListProducts(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
#place Order
class PlaceOrder(APIView):
    def post(self, request):
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
#get order by
class GetOrderBy(APIView):
    def get(self, request, pk):
        order=Order.objects.get(pk=pk)
        serializer=OrderSerializer(order)
        return Response(serializer.data)
#create Category
class CreateCategory(APIView):
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)
#list categories
class ListCategoriers(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
#create Review
class Createreview(APIView):
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
#list review
class ListReview(generics.ListAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    





