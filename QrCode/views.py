from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import qrcode
# Create your views here.

@api_view(["GET", "POST"])
def qr_generator(request):
    
    if request.method == "GET":
        return Response()
    
    elif request.method == "POST":
        data = request.data["data"]
        img = qrcode.make(data)
        img.save("./QrCode/static/qr.png", "PNG")
        context = {"data": data, "image_url" : "qr.png"}
        return render(request, "qrcode_show.html", context=context)