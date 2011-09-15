from django.contrib import admin

from fragments.models import Fragment

class FragmentAdmin(admin.ModelAdmin):
  list_display = ('key',)
  search_fields = ('key', 'content')

admin.site.register(Fragment, FragmentAdmin)
