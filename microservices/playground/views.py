from django.shortcuts import render
from django.http import HttpResponse
import time
import csv
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from queue import Queue, Empty
from threading import Thread, current_thread
import time
import sys
from django.template.loader import get_template
import pyqrcode
import png
from pyqrcode import QRCode
from datetime import datetime
from uuid import uuid4
import base64
from django.utils.html import format_html
from PIL import Image
import glob
from django.template.loader import render_to_string
from django.http import JsonResponse
from fpdf import FPDF
import pytube
# Create your views here.

def home_index(request):
    return render(request, 'home.html')

def master_home(request):
    return render(request, 'master.html')

def qrcode_index(request):
    return render(request, 'qrcode.html')

def qrcode_result(request):
    if request.method == 'POST':
        qr_text = request.POST.get('inputUserText')
        s = qr_text

        # genearte QR code
        url = pyqrcode.create(s)

        #create unique uuid
        eventid = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())

        # create and save the file naming "myqr.png"
        filenamedir = "playground/static/images/" + eventid + ".png"
        final_qr = url.png(filenamedir, scale=6)
        flag = False
        while not flag:
            image_list = []
            for filename in glob.glob(filenamedir):  # assuming gif
                im = Image.open(filename)
                image_list.append(im)
                if image_list:
                    flag = True

        # return HttpResponse with template rendering
        message = render_to_string('ajaxqrcoderesult.html', {'eventid': eventid})
        return HttpResponse(message)


#convert images to pdf

def cip(request):
    return render(request, 'cip.html')

def cip_result(request):
    if request.method == 'POST':
        imagefiles = request.FILES.getlist('files[]', None)
        user_unique_id = request.POST.get('uid',None)
        eventdir = str(datetime.now())
        eventid = (datetime.now()).strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
        for f in imagefiles:
            handle_uploaded_file(f, eventid)

        filenamedir = "playground/static/uploadPdfImages/" + eventid + "*.jpg"
        image_list = []
        for filename in glob.glob(filenamedir):
            im = Image.open(filename)
            im_convert = im.convert('RGB')
            image_list.append(im_convert)
            im_convert.save(r'C:\Users\Daraz\Desktop\djtest\jng\playground\static\uploadPdfImages\pdf/' + eventid + '.pdf', save_all=True, append_images=image_list)

        flag = False
        pdfnamedir = "playground/static/uploadPdfImages/pdf/" + eventid + '.pdf'
        pdf_list = []

        while not flag:
            for filename in glob.glob(pdfnamedir):
                pdf_list.append(filename)
                if pdf_list:
                    flag = True

        message_cip = render_to_string('cipresult.html', {'eventid': eventid})
        return HttpResponse(message_cip)

def handle_uploaded_file(f,eventid):

    with open('playground/static/uploadPdfImages/' + eventid + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def ytv_download(request):
    return render(request, 'ytvdownload.html')

def ytv_download_result(request):
    link = request.POST.get('inputUserText')
    yt = pytube.YouTube(link)
    eventidyoutube = datetime.now().strftime('%Y%m-%d%H-%M%S-') + str(uuid4())
    path = "playground/static/youtubevideo/"
    yt.streams.filter(progressive=True, file_extension='mp4').first().download(path, filename=eventidyoutube+".mp4")

    ytvnamedir = "playground/static/youtubevideo/" + eventidyoutube + ".mp4"
    ytv_list = []
    flag = False
    while not flag:
        for filename in glob.glob(ytvnamedir):
            ytv_list.append(filename)
            if ytv_list:
                flag = True
    message_ytv = render_to_string('ytvdownloadresult.html', {'eventidyoutube': eventidyoutube})
    return HttpResponse(message_ytv)



