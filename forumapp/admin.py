from django.contrib import admin


# Register your models here.
from forumapp.models import Question,Answer,Comment

admin.site.register(Question);
admin.site.register(Answer);
admin.site.register(Comment);

