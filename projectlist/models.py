from django.db import models

# Create your models here.
class AddProjects(models.Model):
    user_email = models.EmailField()
    project_name = models.CharField(max_length=50)
    proj_demo_link = models.CharField(max_length=300)
    proj_source_link = models.CharField(max_length=300)
    tools_used = models.CharField(max_length=250)
    project_description = models.CharField(max_length=500)
    remarks = models.TextField()
    pub_date = models.DateTimeField()
    feedback = models.TextField()
    feedback_deploy = models.TextField()


    def __str__(self):
        return self.project_name

        


class AddUsersInfo(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.user_name



class AddArticles(models.Model):
    user_image = models.ImageField(upload_to='images/')
    article_topic = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    article_image = models.ImageField(upload_to='images/')
    article_link = models.CharField(max_length=250)
    article_description = models.CharField(max_length=450)


    def __str__(self):
        return self.article_topic

    def startsummary(self):
        return self.article_description[:135]
    
    def endsummary(self):
        return self.article_description[135: -1]


