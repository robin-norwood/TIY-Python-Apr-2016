from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from simplecontent.models import Article

class ArticlesTestCase(TestCase):
    def setUp(self):
        Article.objects.create(title="Test #1")
        Article.objects.create(title="Test #2")
        Article.objects.create(title="Test #3")

    def testArticleFields(self):
        #first = Article.objects.create(title="Test #1")
        first = Article.objects.get(title="Test #1")
        self.assertEquals("Test #1", first.title)

    def testGetArticles(self):
        arts = Article.objects.all()
        self.assertEquals(3, len(arts))

    def testArticleIndex(self):
        client = Client()
        resp = client.get('/articles/')
        self.assertEquals(200, resp.status_code)
        self.assertContains(resp, "Showing 3 stories")

    def testArticleView(self):
        client = Client()
        art = Article.objects.order_by("-id")[0]
        url = reverse('simplecontent-view_article', args=[art.id])
        resp = client.get(url)
        self.assertContains(resp, art.title)
