from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    path = 'C:\python\Django\\third-project\\task1\inflation_russia.csv'
    with open(path, encoding="UTF8", newline='') as f:
        reader = csv.reader(f)
        list_str = [row[0] for row in reader]
        head = list_str[0].split(';')
        body = list_str[1:]

    context = {'data': body, 'head': head}

    return render(request, template_name, context=context)