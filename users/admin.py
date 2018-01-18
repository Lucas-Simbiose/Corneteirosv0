from django.contrib import admin
from users.models import Profile, TeamData, TeamCrest, TeamShirt, RealTournament, UserTournament

# Register your models here.
admin.site.register(Profile)
admin.site.register(TeamData)
admin.site.register(TeamCrest)
admin.site.register(TeamShirt)
admin.site.register(RealTournament)
admin.site.register(UserTournament)