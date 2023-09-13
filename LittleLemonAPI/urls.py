from django.urls import path, include
from . import views

urlpatterns = [
    #  Menu-items endpoints
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),

    # User group management endpoints
    path('groups/manager/users', views.GroupViewSet.as_view()),
    path('groups/manager/users/<int:pk>', views.GroupViewSet.as_view()),
    path('groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view()),
    path('groups/delivery-crew/users/<int:pk>', views.DeliveryCrewViewSet.as_view()),

    # Cart management endpoints 
    path('cart/menu-items', views.CartView.as_view()),

    #category
    path('category', views.CategoriesView.as_view()),

    # Order management endpoints
    path('orders', views.OrderView.as_view()),
    path('orders/<int:pk>', views.OrderView.as_view()),
]
