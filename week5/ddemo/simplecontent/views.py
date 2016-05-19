from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponsePermanentRedirect, HttpResponseRedirect, JsonResponse, FileResponse
from django.template import loader
from .models import Article, SuperHero

def gimme_image(request):
    response = FileResponse(open('example.png', 'rb'), content_type='image/png')
#    response['']

    return response

def gimme_jason(request):
    return JsonResponse({"key": "value"})

def search_view(request):
    return HttpResponsePermanentRedirect('https://google.com')

def maint_view(request):
    return HttpResponseRedirect('/articles/maintenance')

def myview(request):
    response = HttpResponse("<h1>Welcome</h1>")
    response.write("<p>This is my website. I hope you like it. Be my friend.</p>")

    return response

def text_file_view(request):
    response = HttpResponse("Here's a text file\n", content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="textfile.txt"'

    response.write("Are you sure you don't want to me my friend? I like cats.")

    return response

def index(request): # HttpRequest
    recent_articles = Article.objects.order_by('-publish_date')[:5]
#    templ = loader.get_template('simplecontent/articles_index.html')

    context = {'recent_articles': recent_articles}

    return render(request, 'simplecontent/articles_index.html', context)

def view_article(request, article_id):

    try:
        article_id = int(article_id)
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("No such article!")
    context = { 'article': article }

    return render(request, 'simplecontent/article_details.html', context)

def cover_photo(request, article_id, image_type="jpg"):
    # article_id = "12"
    # image_type = "bmp"
    if image_type not in ['bmp', 'png', 'jpg']:
        return HttpResponseNotFound("No such type")

    try:
        article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("No such article!")

    cover_photo = article.cover_photo
    response = FileResponse(open(article.cover_photo.image.url, 'rb'), content_type='image/' + image_type)

    return response


def heroes_list(request):
    heroes = SuperHero.objects.all()
    context = { 'heroes': heroes }

    return render(request, 'simplecontent/heroes.html', context)

def hero_details(request, hero_id):
    hero = SuperHero.objects.get(id=hero_id)
    context = { 'hero': hero }

    return render(request, 'simplecontent/hero.html', context)
