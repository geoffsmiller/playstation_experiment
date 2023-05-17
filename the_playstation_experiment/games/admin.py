from django.contrib import admin
from games.models import Game, GameCompany, GamePlatform, GameRelease

admin.site.register(GamePlatform)
admin.site.register(GameCompany)


class GameReleaseInlineAdmin(admin.TabularInline):
    model = GameRelease


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [GameReleaseInlineAdmin]
