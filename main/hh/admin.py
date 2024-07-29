from django.contrib import admin

# Register your models here.
from django.contrib import admin

from hh.models import Skills, Company, Vacancy, Resume, Request

admin.site.register(Skills)
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Resume)
admin.site.register(Request)
