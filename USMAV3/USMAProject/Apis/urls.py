from django.urls import path
from . import views

# MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Universities', views.UniversitiesViewSet)












#ARTICLES
router.register('Articles', views.ArticlesViewSet)


router.register('PeopleWorksCategoryViewSet', views.PeopleWorksCategoryViewSet)

#HOB
router.register('Hobs', views.HobsViewSet)
router.register('CoursesViewSet', views.CoursesViewSet)






# VIEWS KWA AJILI YA KUADD
router.register('AddNewProjectView', views.AddNewProjectView)
router.register('AddNewArticleView', views.AddNewArticleView)
router.register('AddNewExpertView', views.AddNewExpertView)
router.register('AddNewWorkView', views.AddNewWorkView)





#--------------HIZI NDIZO MPYA--------------------------

#----------------------FOR ARCHITECTURE--------------------
router.register('ArchitectureCategories', views.ArchitectureCategoriesViewSet)
router.register('AllArchitects', views.AllArchitectsViewSet)
router.register('ForAddingArchitectureWorksSerializer', views.ForAddingArchitectureWorksSerializerViewSet)







urlpatterns = router.urls