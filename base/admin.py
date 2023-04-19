from django.contrib import admin

# Register your models here.

from .models import RoomMember, Detection, Session,Etudiant


admin.site.register(RoomMember)
admin.site.register(Detection)
admin.site.register(Session)
admin.site.register(Etudiant)

