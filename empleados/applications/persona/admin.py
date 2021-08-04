from django.contrib import admin
from .models import Empleado, Habilitades


admin.site.register(Habilitades)


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name'
    )

    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades')
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado, EmpleadoAdmin)
