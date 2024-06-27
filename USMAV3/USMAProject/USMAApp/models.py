from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, username,phone, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")


        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, phone, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            phone=phone,

        )
        user.is_admin=True
        user.is_staff=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  
class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=15)
    profile_image = models.ImageField(upload_to='media/', blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    # Role_Choices = (
    #         ('MULTI TEACHER', 'MULTI TEACHER'),
    #         ('PHYSICS TEACHER', 'PHYSICS TEACHER'),
    #         ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'),
    #         ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'),
    #         ('ENGLISH TEACHER', 'ENGLISH TEACHER'),
    #         ('CIVICS TEACHER', 'CIVICS TEACHER'),
    #         ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'),
    #         ('HISTORY TEACHER', 'HISTORY TEACHER'),
    #         ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'),
    #         ('KISWAHILI TEACHER', 'KISWAHILI TEACHER'),
    #     )

    # role=models.CharField(verbose_name="role", choices=Role_Choices, max_length=50)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username','phone']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Universities(models.Model):

    UniversityName = models.CharField(max_length=200)
    UniversityPlace = models.CharField(max_length=100,blank=True,null=True)
    UniversityImage = models.ImageField(upload_to='media/UniversityImage/',blank=True,null=True)
    UniversityLink = models.CharField(max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)


    class Meta:
    	verbose_name_plural = "Universities"

    def __str__(self):
    	return self.UniversityName


#HII NI KWA AJILI YA APIS INATUMIA HII MODEL TU KWA KOZI ZOTE
class UniversityCourses(models.Model):

    university = models.ForeignKey(Universities,max_length=200,on_delete=models.CASCADE)
    CourseName = models.CharField(max_length=100,blank=True,null=True)
    CourseImage = models.ImageField(upload_to='media/UniversityImage/',blank=True,null=True)
    CourseDepartment = models.CharField(max_length=100,blank=True,null=True)
    CourseCapacity = models.IntegerField(blank=True,null=True)
    CourseLink = models.CharField(max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "UniversityCourses"

    def __str__(self):
        return self.CourseName



#HIZI NI KWA AJILI YA TEMPLATES INATIMA HIZI MODEL ZOTE
#KWA KILA CHUO






class Modules(models.Model):

    university = models.ManyToManyField(Universities,max_length=200)
    course = models.ForeignKey(UniversityCourses,max_length=200,on_delete=models.CASCADE)
    ModuleName = models.CharField(max_length=100,blank=True,null=True)
    Year = models.CharField(default="First Year",max_length=100,blank=True,null=True)
    ModuleImage = models.ImageField(upload_to='media/ModuleImage/',blank=True,null=True)
    ModuleLink = models.CharField(max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "Modules"

    def __str__(self):
        return self.ModuleName


class AllProjects(models.Model):

    university = models.ForeignKey(Universities,max_length=200, on_delete=models.CASCADE)
    CourseName = models.ForeignKey(UniversityCourses, max_length=100,on_delete=models.CASCADE, blank=False,null=False)
    ProjectName = models.CharField(max_length=500,blank=False,null=False)
    StudentName = models.CharField(max_length=100,blank=False,null=False)
    Year = models.CharField(max_length=50,blank=False,null=False)
    ProjectBody = RichTextUploadingField(blank=True,null=True)
    # ProjectLink = models.CharField(max_length=500,blank=True,null=True)
    pdf = models.FileField(upload_to="media/ProjectsPDF",blank=True,null=True)
    
    Gender_Choices = (
        ('Male','Male'),
        ('Female', 'Female')
        )


    Gender = models.CharField(max_length=100,choices=Gender_Choices, blank=True,null=True)
    
    ProjectImage = models.ImageField(upload_to='media/ProjectImage/',blank=True,null=True)
    
    
    # VideoLink = models.CharField(default="www.youtube.com/dimosojunior", max_length=200,blank=True,null=True)
    StudentEmail = models.EmailField(default="youremail@gmail.com", max_length=100,blank=True,null=True)
    StudentPhoneNumber = models.CharField(default="+255", max_length=50,blank=True,null=True)
    Github = models.CharField(default="https://github.com/dimosojunior/", max_length=1000,blank=True,null=True)
    Youtube = models.CharField(default="www.youtube.com", max_length=1000,blank=True,null=True)
    WhatsappLink = models.CharField(default="www.whatsapp.com", max_length=1000,blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "AllProjects"

    def __str__(self):
        return self.ProjectName



class Articles(models.Model):

    ArticlesName = models.CharField(max_length=1000,blank=False,null=False)
    ArticleImage = models.ImageField(upload_to='media/ArticlesImage/',blank=True,null=True)
    ArticleLink = models.CharField(default="USMA/", max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.ArticlesName


# HII NI KWA AJILI YA APIS NA TEMPLATES 
#ILA KWENYE API KUNA MAREKEBISHO YANATAKIWA KUFANYWA
class ArticlesCategory(models.Model):

    ArticlesName = models.ForeignKey(Articles,on_delete=models.CASCADE, max_length=1000,blank=False,null=False)
    Title = models.CharField(default="How to start learning ---------",max_length=1000,blank=False,null=False)
    WrittenBy = models.CharField(default="Dimoso Junior",max_length=100,blank=True,null=True)
    ArticleBody = RichTextUploadingField(blank=True,null=True)
    ArticleImage = models.ImageField(upload_to='media/ArticlesImage/',blank=True,null=True)
    Github = models.CharField(default="www.github.com",max_length=1000,blank=True,null=True)
    Youtube = models.CharField(default="www.youtube.com",max_length=1000,blank=True,null=True)
    year = models.CharField(default="2023",max_length=100,blank=True,null=True)
    pdf = models.FileField(upload_to="media/ArticlesPDF/",blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ArticlesCategory"

    def __str__(self):
        return self.ArticlesName.ArticlesName





class Hob(models.Model):

    
    CategoryName = models.CharField(max_length=1000,blank=False,null=False)
    CategoryImage = models.ImageField(upload_to='media/HobImage/',blank=True,null=True)
    HobLink = models.CharField(default="USMA/", max_length=500,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Hob"

    def __str__(self):
        return self.CategoryName



#HII NI KWA AJILI YA APIS na  templates
class Experts(models.Model):

    CategoryName = models.ForeignKey(Hob,on_delete=models.CASCADE, max_length=1000,blank=False,null=False)
    StudentName = models.CharField(max_length=500,blank=False,null=False)
    StudentPlace = models.CharField(max_length=100,blank=True,null=True)
    Body = RichTextUploadingField(blank=True,null=True)
    StudentImage = models.ImageField(upload_to='media/Hob/',blank=True,null=True)
    Github = models.CharField(default="www.github.com",max_length=1000,blank=True,null=True)
    Youtube = models.CharField(default="www.youtube.com",max_length=1000,blank=True,null=True)
    Email = models.CharField(default="juniordimoso@gmail.com",max_length=500,blank=True,null=True)
    Instagram = models.CharField(default="www.instagram.com",max_length=1000,blank=True,null=True)
    Whatsapp = models.CharField(default="www.whatsapp.com",max_length=1000,blank=True,null=True)
    Phone = models.CharField(default="+255",max_length=13,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Experts"

    def __str__(self):
        return self.StudentName






# HIZI NI KWA AJILI YA TEMPLATES









class Students(models.Model):

    university = models.ForeignKey(Universities,max_length=200,on_delete=models.CASCADE)
    course = models.ForeignKey(UniversityCourses,max_length=200,on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=100,blank=False,null=False)
    LastName = models.CharField(max_length=100,blank=False,null=False)
    Email = models.EmailField(default="@gmail.com", max_length=100,blank=False,null=False)
    Phone = models.CharField(default="+255", max_length=13,blank=False,null=False)
    StudentImage = models.ImageField(upload_to='media/StudentImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.FirstName + " " + self.LastName


class Teachers(models.Model):

    university = models.ForeignKey(Universities,max_length=200,on_delete=models.CASCADE)
    course = models.ManyToManyField(UniversityCourses,max_length=200)
    FirstName = models.CharField(max_length=100,blank=False,null=False)
    LastName = models.CharField(max_length=100,blank=False,null=False)
    Email = models.EmailField(default="@gmail.com", max_length=100,blank=False,null=False)
    Phone = models.CharField(default="+255", max_length=13,blank=False,null=False)
    TeacherImage = models.ImageField(upload_to='media/StudentImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.FirstName + " " + self.LastName






class ContactMe(models.Model):
    FullName = models.CharField(max_length=200, blank=False, null=False)
    Message = models.TextField(max_length=5000, blank=True, null=True)
    Phone = models.CharField(default='+255',max_length=13, blank=False, null=False)
    Email = models.EmailField(default='@gmail.com', blank=False, null=False)
    Place = models.CharField(max_length=200, blank=False, null=False)
    
    send_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    #to_dimoso_email = models.EmailField(default='juniordimoso8@gmail.com', blank=True, null=True)

    def __str__(self):
        return self.FullName
    class Meta:
        verbose_name_plural = "ContactMe"




class PeopleWorksCategory(models.Model):

    
    CategoryName = models.CharField(max_length=1000,blank=False,null=False)
    CategoryImage = models.ImageField(upload_to='media/PeopleWorksImages/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "PeopleWorksCategory"

    def __str__(self):
        return self.CategoryName


class PeopleWorks(models.Model):

    Category = models.ForeignKey(PeopleWorksCategory,on_delete=models.CASCADE, max_length=1000,blank=False,null=False)
    Title = models.CharField(max_length=1000,blank=False,null=False)
    CreatedBy = models.CharField(default="Dimoso Junior",max_length=100,blank=False,null=False)
    Description = RichTextUploadingField(blank=True,null=True)
    WorkImage = models.ImageField(upload_to='media/PeopleWorksImage/',blank=True,null=True)
    Github = models.CharField(default="www.github.com",max_length=1000,blank=True,null=True)
    Youtube = models.CharField(default="www.youtube.com",max_length=1000,blank=True,null=True)
    Year = models.CharField(default="2024",max_length=100,blank=True,null=True)
    Email = models.CharField(default="juniordimoso@gmail.com",max_length=500,blank=True,null=True)
    Instagram = models.CharField(default="www.instagram.com",max_length=1000,blank=True,null=True)
    Whatsapp = models.CharField(default="www.whatsapp.com",max_length=1000,blank=True,null=True)
    Phone = models.CharField(default="+255",max_length=13,blank=True,null=True)
    pdf = models.FileField(upload_to="media/PeopleWorksPDF/",blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "PeopleWorks"

    def __str__(self):
        return self.Title













#-----------------HIZI ZA CHINI NDO MPYA ----------------

class InformUsers(models.Model):
    Title = models.CharField(max_length=500, blank=False, null=False)
    Message = RichTextUploadingField(blank=True, null=True)     
    post_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def __str__(self):
        return self.Title 

    class Meta:
        verbose_name_plural = "InformUsers"
















#------------------FOR ARCHITECTURE--------------------------


# 1.planning
# 2.michoro



class ArchitectureCategories(models.Model):

    CategoryName = models.CharField(max_length=1000,blank=False,null=False)
    CategoryImage = models.ImageField(upload_to='media/ArchitectureImage/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "ArchitectureCategories"

    def __str__(self):
        return self.CategoryName



class AllArchitects(models.Model):

    ArchitectName = models.CharField(max_length=1000,blank=False,null=False)
    ArchitectImage = models.ImageField(upload_to='media/ArchitectureImage/',blank=True,null=True)
    Location = models.CharField(max_length=100,blank=True,null=True)
    Description = RichTextUploadingField(blank=True,null=True)
    
    Github = models.CharField(max_length=1000,blank=True,null=True)
    Youtube = models.CharField(max_length=1000,blank=True,null=True)
    Email = models.CharField(max_length=500,blank=True,null=True)
    Whatsapp = models.CharField(max_length=1000,blank=True,null=True)
    Phone = models.CharField(max_length=13,blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)




    class Meta:
        verbose_name_plural = "All Architects"

    def __str__(self):
        return self.ArchitectName

# HII NI KWA AJILI YA APIS NA TEMPLATES 
#ILA KWENYE API KUNA MAREKEBISHO YANATAKIWA KUFANYWA
class ArchitectureWorks(models.Model):

    CategoryName = models.ForeignKey(ArchitectureCategories,on_delete=models.CASCADE, max_length=1000,blank=False,null=False)
    ArchitectName = models.ForeignKey(AllArchitects,on_delete=models.CASCADE, max_length=1000,blank=False,null=False)

    Title = models.CharField(max_length=10000,blank=False,null=False)
    Year = models.CharField(max_length=100,blank=True,null=True)
    Description = RichTextUploadingField(blank=True,null=True)
    MainImage = models.ImageField(upload_to='media/ArchitectureImage/',blank=True,null=True)
    FrontViewImage = models.ImageField(upload_to='media/ArchitectureImage/',blank=True,null=True)
    BackViewImage = models.ImageField(upload_to='media/ArchitectureImage/',blank=True,null=True)
    LeftSideViewImage = models.ImageField(upload_to='media/ArchitectureImage/',blank=True,null=True)
    RightSideViewImage = models.ImageField(upload_to='media/ArchitectureImage/',blank=True,null=True)
    TopViewImage = models.ImageField(upload_to='media/ArchitectureImage/',blank=True,null=True)

    pdf = models.FileField(upload_to="media/ArchitecturePDF/",blank=True,null=True)

    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "ArchitectureWorks"

    def __str__(self):
        return self.Title

