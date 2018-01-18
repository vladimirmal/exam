from rest_framework import serializers
from .models import Categories, User, Order, Basket, Products, ProductVersion, Profile


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion
        exclude = ()


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ()


class OrderSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        exclude = ()
        fields = ('user', 'address', 'product', 'date_time')

    def create(self, validated_data):
        user = validated_data['user']
        address = validated_data['address']
        product = validated_data['product']
        date_time = validated_data['date_time']
        order = Order(
            user=user,
            address=address,
            product=product,
            date_time=date_time
        )
        Basket.objects.filter(id=product.id).update(buy=True)
        order.save()
        return order


class BasketSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    cost = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=6)
    buy = serializers.BooleanField(read_only=True, default=False)

    class Meta:
        model = Basket
        exclude = ()
        fields = ('user', 'number', 'elements', 'cost', 'buy')

    def create(self, validated_data):
        user = validated_data['user']
        number = validated_data['number']
        elements = validated_data['elements']
        buy = validated_data['buy']
        need_product = ProductVersion.objects.get(title=elements)
        element = Basket(
            user=user,
            number=number,
            elements=elements,
            cost=need_product.cost * number,
            buy=buy
        )
        element.save()
        return element


class ProfileSerializers(serializers.ModelSerializer):


    class Meta:
        model = User


class HistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ()


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'last_login',
            'date_joined',
            'is_active',
            'groups',
            'user_permissions',
        )

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
