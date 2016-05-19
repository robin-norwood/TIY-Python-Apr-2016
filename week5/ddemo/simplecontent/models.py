from django.db import models
from django.contrib.auth.models import User

# art = Article(category=5)
# art.category # int(5)

class Article(models.Model):
    ARTICLE_CATS = (
    ("LIFESTYLE", 'Lifestyle'),
    ("VARIETY", 'Variety'),
    ("POOLITICS", 'Politics')
    )
    category = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        choices=ARTICLE_CATS,
        default=3)

    title = models.CharField(max_length=128)
    article_text = models.TextField(null=False, blank=False)
    current = models.BooleanField(null=False, default=True, db_index=True)
    slug = models.SlugField(null=False, db_index=True)
    views = models.PositiveIntegerField(null=False, default=0)
    authors = models.ManyToManyField(User)
    cover_photo = models.OneToOneField('Photo', null=True, related_name='cover_photo')
    photos = models.ManyToManyField('Photo')

#    powers = models.ManyToManyField('Power')
    publish_date = models.DateTimeField(auto_now_add=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ": " + self.title

class SuperHero(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def get_powers(self):
        return self.superheropower_set.all()

    def add_power(self, name, level):
        power = Power.objects.get(name=name)
        shp = SuperHeroPower.create(hero=self, power=power, level=level)

class SuperHeroPower(models.Model):
    hero = models.ForeignKey('SuperHero')
    power = models.ForeignKey('Power')
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.hero.name + " " + self.power.name + " level: " + str(self.level)

class Power(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    #value = models.IntegerField()

class Comment(models.Model):
    comment_text = models.TextField(max_length=2000, blank=False)
    moderated = models.BooleanField(default=False, null=False)
    likes = models.PositiveIntegerField(default=0, null=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Photo(models.Model):
    image = models.ImageField()
    photographer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    caption = models.CharField(max_length=256)

    def __str__(self):
        return str(self.id)
