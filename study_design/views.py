import json

import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def study_design(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, 'study_design/study_design.html', context=context)
    elif request.method == 'POST':
        params = {
            "title": "TEST TITLE",
            "degree": 4
        }
        res = requests.post('http://127.0.0.1:8080', json.dumps(params))

        print("\n\n")
        print("res :: ", res.json())
        print("\n\n")
        return HttpResponse('<a href="/">되돌아가기</a> ', status=200)
