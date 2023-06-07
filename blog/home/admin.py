from django.contrib import admin
from home.models import Blog,Contact


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css={
            "all":('/static/css/adm.css',)
        }
        js=('/static/js/blog.js',)

admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact)
