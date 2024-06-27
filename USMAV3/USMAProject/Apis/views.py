from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from Apis.serializers import *
from USMAApp.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet


from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser

# Create your views here.



#-----------------------------MODEL VIEW SETS-----------------------------------

#-------KWA AJILI YA  ALL UNIVERSTIES--------------
class UniversitiesViewSet(ModelViewSet):
	queryset = Universities.objects.all()
	serializer_class = UniversitiesSerializer
	# permission_classes=[IsAuthenticated]


class CoursesViewSet(ModelViewSet):
	queryset = UniversityCourses.objects.all()
	serializer_class = UniversityCoursesSerializer
	# permission_classes=[IsAuthenticated]
	

# FILTER ALL COURSE MODEL FOR SPECIFIC UNIVERSITY


























	# ---------------------ARTICLES-------------------------------


class ArticlesViewSet(ModelViewSet):
	queryset = Articles.objects.all()
	serializer_class = ArticlesSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	#pagination_class = PageNumberPagination


  # -------------------AI---------------



class PeopleWorksCategoryViewSet(ModelViewSet):
	queryset = PeopleWorksCategory.objects.all()
	serializer_class = PeopleWorksCategorySerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	#pagination_class = PageNumberPagination





	# ---------------------HOB-------------------------------


class HobsViewSet(ModelViewSet):
	queryset = Hob.objects.all()
	serializer_class = HobSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination











# KWA AJILI YA KUADD NEW PROJECT
class AddNewProjectView(ModelViewSet):
    queryset = AllProjects.objects.all()
    serializer_class = AllProjectsSerializer


class AddNewArticleView(ModelViewSet):
    queryset = ArticlesCategory.objects.all()
    serializer_class = ArticlesCategorySerializer

class AddNewExpertView(ModelViewSet):
    queryset = Experts.objects.all()
    serializer_class = ExpertsSerializer



class AddNewWorkView(ModelViewSet):
    queryset = PeopleWorks.objects.all()
    serializer_class = PeopleWorksSerializer












#-----------HIZI NDIZO MPYA_----------------------------
class ArchitectureCategoriesViewSet(ModelViewSet):
	queryset = ArchitectureCategories.objects.all()
	serializer_class = ArchitectureCategoriesSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	#pagination_class = PageNumberPagination

class AllArchitectsViewSet(ModelViewSet):
	queryset = AllArchitects.objects.all()
	serializer_class = AllArchitectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	#pagination_class = PageNumberPagination


class ForAddingArchitectureWorksSerializerViewSet(ModelViewSet):
	queryset = ArchitectureWorks.objects.all()
	serializer_class = ArchitectureWorksSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	#pagination_class = PageNumberPagination


