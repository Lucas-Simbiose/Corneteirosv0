from django.contrib import admin
from users.models import Profile, TeamData, TeamCrest, TeamShirt, RealTournament, UserTournament, SoccerTeam, \
    TeamTournament, Round, Match, Hint

# Register your models here.
admin.site.register(Profile)
admin.site.register(TeamData)
admin.site.register(TeamCrest)
admin.site.register(TeamShirt)
admin.site.register(RealTournament)
admin.site.register(UserTournament)
admin.site.register(SoccerTeam)
admin.site.register(TeamTournament)
admin.site.register(Round)
admin.site.register(Match)
admin.site.register(Hint)