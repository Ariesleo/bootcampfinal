from django.forms import ModelForm
from .models import AddProjects, AddArticles, AddUsersInfo

class AddProjectsForm(ModelForm):
    class Meta:
        model = AddProjects
        fields = ['project_name','proj_demo_link','proj_source_link','tools_used','project_description','remarks','feedback_deploy']
        
        
        #fields = ['feedback'] #if only want feedback


class AddFeedbackForm(ModelForm):
    class Meta:
        model = AddProjects
        fields = ['feedback']



class AddArticlesForm(ModelForm):
    class Meta:
        model = AddArticles
        fields = ['user_image','article_topic','article_image','article_link','article_description']



class AddUsersInfoForm(ModelForm):
    class Meta:
        model = AddUsersInfo
        fields = '__all__'