from rest_framework import serializers

from .models import Portfolio

# class PersonSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Person
#        fields = ('name', 'birth_year', 'eye_color', 'species')

# date = models.DateTimeField(blank=True, null=True)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     description = models.CharField(max_length=500, blank=True, null=True)
#     body = RichTextField(blank=True, null=True)
#     image = models.ImageField(blank=True, null=True, upload_to="portfolio")
#     slug = models.SlugField(null=True, blank=True)
#     is_active = models.BooleanField(default=True)

class PortfolioSerializer(serializers.ModelSerializer):
   class Meta:
       model = Portfolio
       fields = ('date', 'description', 'body', 'image', 'slug', 'is_active')