from unicodedata import name
from django.urls import path
from . import views
from django.conf.urls.static import static
# from . import custom_view
# from . import custom_daraz
# from . import custom_amazon

#urlConf
urlpatterns = [
    path('', views.master_home, name="master_home"),
    # path('home/', views.home_index, name="home"),
    path('home/', views.master_home, name="home"),
    path('master/', views.master_home, name="master"),
    path('qrcode/', views.qrcode_index, name="qrcode"),
    path('qrcoderesult/', views.qrcode_result, name="qrcoderesult"),
    path('convert-image-to-pdf/', views.cip, name="convert_image_to_pdf"),
    path('convert-image-to-pdf-result/', views.cip_result, name="convert_image_to_pdf_result"),
    path('youtube-video-download/', views.ytv_download, name="youtube_video_download"),
    path('youtube-video-download-result/', views.ytv_download_result, name="youtube_video_download_result"),
]

