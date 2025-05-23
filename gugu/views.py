from django.shortcuts import render

from django.http import HttpResponse

def gugu(request, number):  # ✅ 함수 이름이 정확히 gugu여야 합니다
    result = ""
    for i in range(1, 10):
        result += f"{number} x {i} = {number * i}<br>"
    return HttpResponse(result)

# Create your views here.
