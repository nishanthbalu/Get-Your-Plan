from django.contrib import admin

# Register your models here.
from .models import user_login, user_details, architect_details, plan_settings, architect_plans
from .models import plan_details, user_search, user_proposal, user_rating, sales_master



admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(architect_details)
admin.site.register(plan_settings)
admin.site.register(architect_plans)
admin.site.register(plan_details)
admin.site.register(user_search)
admin.site.register(user_proposal)
admin.site.register(user_rating)
admin.site.register(sales_master)