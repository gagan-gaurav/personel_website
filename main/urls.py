from django.urls import path, include
from rest_framework import routers
from .views import PortfolioViewSet
from . import views

app_name = "main"

router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioViewSet)

urlpatterns = [
	path('', views.IndexView.as_view(), name = "home"),
	path('contact/', views.ContactView.as_view(), name = "contact"),
	path('portfolio/', views.PortfolioView.as_view(), name = "portfolios"),
	path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name = "portfolio"),
	path('blog/', views.BlogView.as_view(), name = "blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name = "blog"),
	path('api/portfolio/', include(router.urls)),
]