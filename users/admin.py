from django.contrib import admin
from users.models import Profile, TeamData, TeamCrest, TeamShirt

# Register your models here.
admin.site.register(Profile)
admin.site.register(TeamData)
admin.site.register(TeamCrest)
admin.site.register(TeamShirt)