from django.shortcuts import render
#View for index page.
def page(request):
    new_project = Project(title = "Tasks Manager with Django", 
            description = "Django project to getting start with Django
            easily.", client_name = "Me")
    new_project.save()
    return render(request, 'en/public/index.html', {'action': 'Save dates
    of model'})
