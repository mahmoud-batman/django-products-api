from products.models import Product
from rest_framework import viewsets, permissions
from .serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


# class SlugProductViewSet(viewsets.ModelViewSet):
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = ProductSerializer

#     def get_queryset(self, slug):
#         """
#         This view should return a list of all the purchases for
#         the user as determined by the username portion of the URL.
#         """
#         # slug = self.kwargs['slug']
#         print("slug")
#         return Product.objects.filter(category=slug)
