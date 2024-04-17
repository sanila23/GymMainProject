from django.contrib import admin
from gym.models import *
from import_export.admin import ImportExportModelAdmin


admin.site.register(Bill)
admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(Diet)
admin.site.register(Schedule)
admin.site.register(Store)