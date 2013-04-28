from django.contrib import admin

from .models import (
	BusinessCategory,
	Business,
	Motivation,
	Purchase,
	)

admin.site.register(BusinessCategory)
admin.site.register(Business)
admin.site.register(Motivation)
admin.site.register(Purchase)