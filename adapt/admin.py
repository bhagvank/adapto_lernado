from django.contrib import admin

from .models import SlackUser
from .models import Recommendation

class SlackUserAdmin(admin.ModelAdmin):
	
    class Meta:
        model = SlackUser
        
class RecommendationAdmin(admin.ModelAdmin):
	
    class Meta:
        model = Recommendation       
 
admin.site.register(SlackUser,SlackUserAdmin)
admin.site.register(Recommendation,RecommendationAdmin)





