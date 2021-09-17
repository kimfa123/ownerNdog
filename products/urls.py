from django.urls import path

form products.views import ProducteView


urlpatterns = [
	path('', ProductsView.as_view()),
]
