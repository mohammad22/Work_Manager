from django.shortcuts import render
from TasksManager.models import Project

#View for index page.
def page(request):
    new_project = Project(title = "Tasks Manager with Django", description = "Django project to getting start with Django easily.", client_name = "Me")
    new_project.save()
<<<<<<< Updated upstream
    return render(request, 'en/public/index.html', {'action': 'Save dates of model'})
=======
    return render(request, 'en/public/index.html', {'action': 'Save datas of model'})
>>>>>>> Stashed changes
