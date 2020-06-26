from django.shortcuts import render, redirect
from django.utils import timezone
from . models import AddProjects, AddUsersInfo, AddArticles
from .forms import AddProjectsForm, AddFeedbackForm, AddArticlesForm, AddUsersInfoForm

# Create your views here.

def addproject(request):
    if request.method == 'POST':
        if request.POST['user_email'] and request.POST['project_name'] and request.POST['project_demo_link'] and request.POST['project_source_link'] and request.POST['tools_used'] and request.POST['project_description']:
            user_email = request.POST['user_email']
            project_name = request.POST['project_name']
            project_demo_link = request.POST['project_demo_link']
            project_source_link = request.POST['project_source_link']
            tools_used = request.POST['tools_used']
            project_description = request.POST['project_description']
            remarks = request.POST['remarks']
            pub_date = timezone.datetime.now()

            query = AddProjects()

            query.user_email = user_email

            query.project_name = project_name
            obj = AddProjects.objects.filter(project_name = project_name)
            if obj.exists():
                return render(request, 'projectlist/addproject.html', {'error': 'Project Name already exists please use different One'})

            
        
            if project_demo_link.startswith('http://') or project_demo_link.startswith('https://'):
                query.proj_demo_link = project_demo_link
            else:
                 query.proj_demo_link = 'https://' + project_demo_link

            if project_source_link.startswith('http://') or project_source_link.startswith('https://'):
                query.proj_source_link = project_source_link
            else:
                query.proj_source_link ='https://' + project_source_link

            query.tools_used = tools_used
            query.project_description = project_description
            query.remarks = remarks
            query.pub_date = pub_date

            query.save()

            obj1 = AddUsersInfo.objects.filter(user_email=user_email)
            if not obj1.exists():
                return render(request, 'projectlist/adduser.html', {'newuser': 'Seems you are adding project for the first time please fill the info below'})

            return redirect('showprojectlist')
        else:
            return render(request,'projectlist/addproject.html', {'error_field_empty': '!!!!!!---all the requirements need to be filled---!!!!!!!!'})
    else:
        return render(request,'projectlist/addproject.html')





def adduser(request):
    if request.method == 'POST':
        if request.POST['user_name'] and request.POST['user_email'] and request.FILES['user_image']:
            user_name = request.POST['user_name']
            user_email = request.POST['user_email']
            user_image = request.FILES['user_image']

            query = AddUsersInfo()

            obj1 = AddUsersInfo.objects.filter(user_name = user_name)
            if obj1.exists():
                return render(request, 'projectlist/adduser.html', {'username_error': '!!!!--The user name has already been taken use different one--!!!!'})
            else:
                query.user_name = user_name

            obj = AddProjects.objects.filter(user_email = user_email)
            if not obj.exists():
                return render(request, 'projectlist/adduser.html', {'email_error': '!!!!--The email adress you entered did not match. So please use same email--!!!!'})
            else:
                query.user_email = user_email

            query.user_image = user_image

            query.save()
            return redirect('showprojectlist') #best listproject.html file ma lanu pparxa
        else:
            return render(request, 'projectlist/adduser.html', {'error_field_empty': '!!!!----All the fields are required----!!!!'})
    else:
        return render(request,'projectlist/adduser.html')




def addarticle(request):
    #return render(request,'projectlist/addproject.html', {'error_art': '!!!!----All feilds are required----!!!!'})
    if request.method == 'POST':
        if request.FILES['users_image'] and request.POST['article_topic'] and request.FILES['article_image'] and request.POST['article_link'] and request.POST['article_description']:
            users_image = request.FILES['users_image']
            article_topic = request.POST['article_topic']
            pub_date = timezone.datetime.now()
            article_image = request.FILES['article_image']
            article_link = request.POST['article_link']
            article_description = request.POST['article_description']

            query = AddArticles()
            query.user_image = users_image
            query.article_topic = article_topic
            query.pub_date = pub_date
            query.article_image = article_image


            if article_link.startswith('http://') or article_link.startswith('https://'):
                query.article_link = article_link
            else:
                query.article_link ='https://' + article_link


            query.article_description = article_description

            query.save()
            return redirect('showarticle')
         
        else:
            return render(request,'projectlist/addproject.html', {'error_art': '!!!!----All feilds are required----!!!!'})
    else:
        return render(request, 'projectlist/addproject.html')






def showprojectlist(request):
    add_projects = AddProjects.objects
    add_users = AddUsersInfo.objects
    return render(request, 'projectlist/showprojects.html', {'add_users':add_users, 'add_projects': add_projects})



def showarticle(request):
    add_article = AddArticles.objects
    return render(request, 'projectlist/article.html', {'add_article': add_article})




def listupdate(request, pk=id):

    updateproj = AddProjects.objects.get(id = pk)
    form = AddProjectsForm(instance=updateproj)

    if request.method == 'POST':
        form = AddProjectsForm(request.POST, instance=updateproj)
        if form.is_valid():
            form.save()
            return redirect('showprojectlist')
    context = {'form': form}
    return render(request, 'projectlist/updatelist.html', context)


def feedbackupdate(request, pk=id):
    addfeedback = AddProjects.objects.get(id = pk)
    form = AddFeedbackForm(instance=addfeedback)

    if request.method =='POST':
        form = AddFeedbackForm(request.POST, instance=addfeedback)
        if form.is_valid():
            form.save()
            return redirect('showprojectlist')
    context = {'form': form}
    return render(request, 'projectlist/addfeedback.html', context)



def projectdelete(request, pk=id):
    item = AddProjects.objects.get(id = pk)

    if request.method == 'POST':
        item.delete()
        return redirect('showprojectlist')
    context = {'item': item}
    return render(request, 'projectlist/deleteproject.html', context)


#code below update the article content i.e card content
def updatearticle(request, pk=id):

    updateartic = AddArticles.objects.get(id=pk)
    form = AddArticlesForm(instance=updateartic)
    if request.method == 'POST':
        form = AddArticlesForm(request.POST, instance=updateartic)
        if form.is_valid():
            form.save()
            return redirect('showarticle')
    context = {'form': form}
    return render(request, 'projectlist/updatecard.html', context)

#update the user info
def updateUsers(request, pk=id):
    userupdate = AddUsersInfo.objects.get(id=pk)
    form = AddUsersInfoForm(instance=userupdate)
    if request.method == 'POST':
        form = AddUsersInfoForm(request.POST, instance=userupdate)
        if form.is_valid():
            form.save()
            return redirect('showprojectlist')
    context = {'form': form}
    return render(request, 'projectlist/updateuser.html', context)

#delete the entire card
def cardDelete(request, pk=id):
    carditem = AddArticles.objects.get(id=pk)

    if request.method == 'POST':
        carditem.delete()
        return redirect('showarticle')
    context = {'carditem': carditem}
    return render(request, 'projectlist/deletecard.html', context)


#delete entire user info

def Userdelete(request, pk=id):

    useritem = AddUsersInfo.objects.get(id=pk)

    if request.method == 'POST':
        useritem.delete()
        return redirect('showprojectlist')
    context = {'useritem':useritem}
    return render(request, 'projectlist/deleteUser.html', context)


#def passid(request, id):
    #idpass = AddArticles.objects.get(pk=id)
    #return render_to_response('projectlist/article.html', {'idpass': idpass})