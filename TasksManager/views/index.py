from django.shortcuts import render
#View for index page.
def page(request):
    my_variable = "blob in the view"
    years_old = 15
    array_city_capitale = ["Paris", "London", "Washington"]
    # the variables can be injected to the template via key:value mechanism
    # here the key is a charstring which will be the name of the variable
    # in the template.
    # the value is the name of an object which its current
    # value will be imported as the value of key into template
    return render(request, 'en/public/index2.html',
                        {"template_var": my_variable,
                         "years": years_old,
                         "array_city": array_city_capitale }
                 )
