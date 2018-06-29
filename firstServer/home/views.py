from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import urllib.request
import json
import datetime
import requests


def keyboard(request):
    return JsonResponse(
        {
            "type" : "buttons",
            "buttons" : ["선택 1", "선택 2", "선택 3"]
        }   
    )


@csrf_exempt
def message(request):
    message = ((request.body).decode('utf-8'))
    return_json_str = json.loads(message)
    return_str = return_json_str['content'] #버튼 항목중 무엇을 눌렀는가

    if return_str == '선택 1':
        return JsonResponse({ #return 밑에는 공통어
            "message": {
               "text": wether()
            }
        })
    if return_str == '선택 2':
        return JsonResponse({ #return 밑에는 공통어
            "message": {
                "text": "돈필요해요"
            }
        })
    if return_str == '선택 3':
        return JsonResponse({ #return 밑에는 공통어
            "message": {
                "text": "돈줘요"
            }
        })
def wether():
    params = {"version": "1", "city":"서울", "county":"광진구","village":"군자동"}
    headers = {"appKey": "f920a656-4102-4024-90e6-92092c1dcf03"}
    response = requests.get("https://api2.sktelecom.com/weather/current/minutely", params=params, headers=headers)
    data = json.loads(response.text)
    return data