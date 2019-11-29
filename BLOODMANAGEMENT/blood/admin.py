from django.contrib import admin
from .models import NeedBlood
from .models import DonateBlood
from .models import AvailableCity
from .models import AvailableBloodGroups
from .models import Blood_Bank
from .models import fact
from .models import Blood_Camps
from .models import chart
# Register your models here.

admin.site.register(NeedBlood)
admin.site.register(DonateBlood)
admin.site.register(AvailableCity)
admin.site.register(Blood_Bank)
admin.site.register(Blood_Camps)
admin.site.register(AvailableBloodGroups)
admin.site.register(fact)
admin.site.register(chart)
