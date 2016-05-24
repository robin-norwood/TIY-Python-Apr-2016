from django.conf.urls import url
from . import views

app_name = 'articles'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<article_id>[0-9]+)/?$', views.view_article, name="view"),
    url(r'^(?P<article_id>[0-9]+)/cover_photo\.?(?P<image_type>png|jpg|bmp)?$',
        views.cover_photo,
        name="cover_photo"),
    url(r'^responsedemo$', views.myview),
    url(r'^myfile$', views.text_file_view),
    url(r'^search$', views.search_view),
    url(r'^news$', views.maint_view),
    url(r'^example\.png$', views.gimme_image)
]

# IN MY HTMLS:

# <img src="/articles/19/cover_photo.jpg"/>

# WILL MATCH
#5/cover_photo.png
#12/cover_photo.bmp

# WILL NOT MATCH
#faefaeafd/cover_photo.bmp
#12/cover_photo
#34/cover_photo.jpeg
#343241/cover_photo.jpg.javascriptsux
#


#    url(r'^(?P<article_id>[0-9]+)/$', views.view_article, name='content-view_article')
