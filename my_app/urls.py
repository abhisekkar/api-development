from django.urls import path
from .views import(
    CreatUser,CreateProduct,CreateCategory,Createreview,ListCategoriers,
    ListProducts,ListReview,GetOrderBy,GetUser,PlaceOrder
)
urlpatterns = [
    path('createuser/',CreatUser.as_view()),
    path('users/',GetUser.as_view()),
    path('createproducts/',CreateProduct.as_view()),
    path('products/',ListProducts.as_view()),
    path('placeorder/',PlaceOrder.as_view()),
    path('order/<int:pk>/',GetOrderBy.as_view()),
    path('createcategory/',CreateCategory.as_view()),
    path('categories/',ListCategoriers.as_view()),
    path('review/createreview/',Createreview.as_view()),
    path('reviews/',ListReview.as_view())
]
