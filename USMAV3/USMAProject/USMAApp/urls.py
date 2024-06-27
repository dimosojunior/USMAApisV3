
from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name="home"),
    path('GetAllUniversities/', views.GetAllUniversitiesView.as_view(), name="GetAllUniversities"),
    path('GetAllUniversitiesCourses/', views.GetAllUniversitiesCoursesView.as_view(), name="GetAllUniversitiesCourses"),
    path('GetAllProjects/', views.GetAllProjectsView.as_view(), name="GetAllProjects"),


    #-----------ARTICLES----------------
    path('GetAllArticles/', views.GetAllArticlesView.as_view(), name="GetAllArticles"),
    path('GetAllArticlesCategory/', views.GetAllArticlesCategoryView.as_view(), name="GetAllArticlesCategory"),


    #-----------HOB----------------
    path('GetAllHob/', views.GetAllHobView.as_view(), name="GetAllHob"),
    path('GetAllExpertCategory/', views.GetAllExpertCategoryView.as_view(), name="GetAllExpertCategory"),

    #-------------------people works---------------------
    path('GetAllPeopleWorksCategory/', views.GetAllPeopleWorksCategoryView.as_view(), name="GetAllPeopleWorksCategory"),
    path('GetAllPeopleWorks/', views.GetAllPeopleWorksView.as_view(), name="GetAllPeopleWorks"),



    #--------------CREATE URLS-------------------
    path('CreateNewProject/', views.CreateNewProject.as_view(), name="CreateNewProject"),
    path('CreateNewArticle/', views.CreateNewArticle.as_view(), name="CreateNewArticle"),
    path('CreateNewExpert/', views.CreateNewExpert.as_view(), name="CreateNewExpert"),
    path('CreateNewWork/', views.CreateNewWork.as_view(), name="CreateNewWork"),






    #HIZI NDO MPYA ZINAANZIA HAPA-------------------------------
    path('', views.InformUsersPage, name="InformUsersPage"),
    path('CountAllProjectsView/', views.CountAllProjectsView.as_view(), name="CountAllProjectsView"),
    path('CountArticlesCategoryView/', views.CountArticlesCategoryView.as_view(), name="CountArticlesCategoryView"),
    path('CountExpertsView/', views.CountExpertsView.as_view(), name="CountExpertsView"),
    path('CountPeopleWorksView/', views.CountPeopleWorksView.as_view(), name="CountPeopleWorksView"),





    #------------------------FOR ARCHITECTURE-------------------
    path('GetAllArchitectsView/', views.GetAllArchitectsView.as_view(), name="GetAllArchitectsView"),
    path('GetAllWorksForEachArcitectView/', views.GetAllWorksForEachArcitectView.as_view(), name="GetAllWorksForEachArcitectView"),
    path('GetAllArchitectureWorksByCategoriesView/', views.GetAllArchitectureWorksByCategoriesView.as_view(), name="GetAllArchitectureWorksByCategoriesView"),


    
]
