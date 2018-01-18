from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.permissions import IsAuthenticated
from exam_app.models import User, Products, Categories, Order, Basket, ProductVersion, Profile
from exam_app.serializers import (
    UserSerializers,
    OrderSerializers,
    ProductSerializers,
    CategorySerializers,
    BasketSerializers,
    HistorySerializers,
)


class CategoryView(GenericViewSet,
                mixins.ListModelMixin):

    serializer_class = CategorySerializers
    queryset = Categories.objects.all()


class ProductView(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin):

    serializer_class = ProductSerializers
    queryset = ProductVersion.objects.all()


class BasketView(GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = BasketSerializers

    def get_queryset(self):
        username = self.request.user

        queryset = Basket.objects.filter(user_id=username)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserView(GenericViewSet,
               mixins.CreateModelMixin):
    serializer_class = UserSerializers

    def get_queryset(self):
        username = self.request.user

        queryset = User.objects.filter(user=username)
        return queryset


class HistoryView(GenericViewSet,
                  mixins.ListModelMixin):
    serializer_class = HistorySerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        username = self.request.user

        queryset = Order.objects.filter(user=username)
        return queryset


class ProfileView(GenericViewSet,

                  mixins.ListModelMixin):
    serializer_class = UserSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        username = self.request.user

        queryset = User.objects.filter(username=username)
        return queryset


class OrderView(GenericViewSet,
                mixins.CreateModelMixin,
                mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializers

    def get_queryset(self):
        username = self.request.user

        queryset = Order.objects.filter(user=username)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




