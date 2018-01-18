from exam_app.views import UserView, ProductView,  BasketView, HistoryView, CategoryView, OrderView, ProfileView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include


router = DefaultRouter()
router.register(r'users', UserView, base_name='user')
router.register(r'category', CategoryView)
router.register(r'basket', BasketView, base_name='basket')
router.register(r'products', ProductView)
router.register(r'orders', OrderView, base_name='order')
router.register(r'profile', ProfileView, base_name='profiles')
router.register(r'profile/history', HistoryView, base_name='history')




urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', obtain_jwt_token)
]
