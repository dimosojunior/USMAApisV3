from USMAApp.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from USMAApp.models import *


# from rest_framework.validators import UniqueValidator
# from rest_framework_jwt.settings import api_settings



#______________DJANGO REACT AUTHENTICATION_________________

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email','phone', 'password')

#______________MWISHO HAPA DJANGO REACT AUTHENTICATION_________________





class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        # fields = ['id', 'username', 'email','phone','first_name','profile_image']












# kwa ajili ya kumregister mtu bila kutumia token
class UserCreationSerializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=25)
	email=serializers.EmailField(max_length=50)
	password=serializers.CharField(max_length=50)


	class Meta:
		model= MyUser
		fields= ['username','email','password']
		#fields='__all__'

	def validate(self,attrs):
		username_exists = MyUser.objects.filter(username=attrs['username']).exists()
		if username_exists:
			raise serializers.ValidationError(detail="User with username already exists")


		email_exists = MyUser.objects.filter(email=attrs['email']).exists()
		if email_exists:
			raise serializers.ValidationError(detail="User with email already exists")

		return super().validate(attrs)


		

class UniversitiesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Universities
		fields = '__all__'


class UniversityCoursesSerializer(serializers.ModelSerializer):

	
	university = UniversitiesSerializer(many=False)

	class Meta:
		model = UniversityCourses
		fields = '__all__'
		# fields = [
		# 'university',
		# 'CourseName',
		# 'CourseImage',
		# 'CourseDepartment',
		# 'CourseCapacity',

		# ]

class AllProjectsSerializer(serializers.ModelSerializer):
	# hizi ni foreign key so badala ya kudisplay number
	# basi idisplay hilo jina la category ndo tunafanya hivi

	#university = UniversitiesSerializer(many=False)
	#CourseName = UniversityCoursesSerializer(many=False)

	class Meta:
		model = AllProjects
		fields = '__all__'

	def create(self, validated_data):
	    pdf = validated_data.pop('pdf', None)
	    image_file = validated_data.pop('ProjectImage', None)
	    project = AllProjects.objects.create(**validated_data)

	    if pdf:
	        project.pdf = pdf
	    if image_file:
	        project.ProjectImage = image_file
	    project.save()
	    return project








class ArticlesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Articles
		fields = '__all__'


class ArticlesCategorySerializer(serializers.ModelSerializer):
	#ilikuona actual ArticlesName name badala ya id unabidi uadd hiki kitu chini
	#ArticlesName = ArticlesSerializer(many=False)

	class Meta:
		model = ArticlesCategory
		fields = '__all__'
		# fields = [
		# "ArticlesName",
		# "Title",
		# "WrittenBy",
		# "ArticleBody",
		# "ArticleImage",
		# "Github",
		# "Youtube",
		# "year",
		# "pdf",
		# ]

	def create(self, validated_data):
	    pdf = validated_data.pop('pdf', None)
	    image_file = validated_data.pop('ArticleImage', None)
	    project = ArticlesCategory.objects.create(**validated_data)

	    if pdf:
	        project.pdf = pdf
	    if image_file:
	        project.ArticleImage = image_file
	    project.save()
	    return project


#----------------------HOB------------------------

class HobSerializer(serializers.ModelSerializer):

	class Meta:
		model = Hob
		fields = '__all__'


class ExpertsSerializer(serializers.ModelSerializer):
	#ilikuona actual CategoryName name badala ya id unabidi uadd hiki kitu chini
	#CategoryName = HobSerializer(many=False)

	class Meta:
		model = Experts
		fields = '__all__'

	def create(self, validated_data):
	    
	    image_file = validated_data.pop('StudentImage', None)
	    project = Experts.objects.create(**validated_data)

	    
	    if image_file:
	        project.StudentImage = image_file
	    project.save()
	    return project





#----------------------people works------------------------

class PeopleWorksCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = PeopleWorksCategory
		fields = '__all__'


class PeopleWorksSerializer(serializers.ModelSerializer):
	#ilikuona actual CategoryName name badala ya id unabidi uadd hiki kitu chini
	#Category = PeopleWorksCategorySerializer(many=False)

	class Meta:
		model = PeopleWorks
		fields = '__all__'

	def create(self, validated_data):
	    
	    image_file = validated_data.pop('WorkImage', None)
	    project = PeopleWorks.objects.create(**validated_data)

	    
	    if image_file:
	        project.WorkImage = image_file
	    project.save()
	    return project

















#-----------------------FOR ARCHITECTURE -------------------
class ArchitectureCategoriesSerializer(serializers.ModelSerializer):

	class Meta:
		model = ArchitectureCategories
		fields = '__all__'



class AllArchitectsSerializer(serializers.ModelSerializer):

	class Meta:
		model = AllArchitects
		fields = '__all__'





class ArchitectureWorksSerializer(serializers.ModelSerializer):
	#ilikuona actual ArticlesName name badala ya id unabidi uadd hiki kitu chini
	CategoryName = ArchitectureCategoriesSerializer(many=False)
	ArchitectName = AllArchitectsSerializer(many=False)

	class Meta:
		model = ArchitectureWorks
		fields = '__all__'
		

	def create(self, validated_data):
		pdf = validated_data.pop('pdf', None)

		MainImage = validated_data.pop('MainImage', None)
		FrontViewImage = validated_data.pop('FrontViewImage', None)
		BackViewImage = validated_data.pop('BackViewImage', None)
		LeftSideViewImage = validated_data.pop('LeftSideViewImage', None)
		RightSideViewImage = validated_data.pop('RightSideViewImage', None)
		TopViewImage = validated_data.pop('TopViewImage', None)

		archi = ArchitectureWorks.objects.create(**validated_data)

		if pdf:
		    archi.pdf = pdf

		if MainImage:
		    archi.MainImage = MainImage

		if FrontViewImage:
		    archi.FrontViewImage = FrontViewImage

		if BackViewImage:
		    archi.BackViewImage = BackViewImage

		if LeftSideViewImage:
		    archi.LeftSideViewImage = LeftSideViewImage

		if RightSideViewImage:
		    archi.RightSideViewImage = RightSideViewImage

		if TopViewImage:
		    archi.TopViewImage = TopViewImage


		archi.save()
		return archi






class ForAddingArchitectureWorksSerializer(serializers.ModelSerializer):
	#ilikuona actual ArticlesName name badala ya id unabidi uadd hiki kitu chini
	# CategoryName = ArchitectureCategoriesSerializer(many=False)
	# ArchitectName = AllArchitectsSerializer(many=False)

	class Meta:
		model = ArchitectureWorks
		fields = '__all__'
		

	def create(self, validated_data):
		pdf = validated_data.pop('pdf', None)

		MainImage = validated_data.pop('MainImage', None)
		FrontViewImage = validated_data.pop('FrontViewImage', None)
		BackViewImage = validated_data.pop('BackViewImage', None)
		LeftSideViewImage = validated_data.pop('LeftSideViewImage', None)
		RightSideViewImage = validated_data.pop('RightSideViewImage', None)
		TopViewImage = validated_data.pop('TopViewImage', None)

		archi = ArchitectureWorks.objects.create(**validated_data)

		if pdf:
		    archi.pdf = pdf

		if MainImage:
		    archi.MainImage = MainImage

		if FrontViewImage:
		    archi.FrontViewImage = FrontViewImage

		if BackViewImage:
		    archi.BackViewImage = BackViewImage

		if LeftSideViewImage:
		    archi.LeftSideViewImage = LeftSideViewImage

		if RightSideViewImage:
		    archi.RightSideViewImage = RightSideViewImage

		if TopViewImage:
		    archi.TopViewImage = TopViewImage


		archi.save()
		return archi