from django.contrib import admin

from manual.models import Manual, ManualElem, ManualVersion


class VersionInline(admin.StackedInline):
    model = ManualVersion
    extra = 1


@admin.register(Manual)
class ManualAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_title')
    list_filter = ('title', )
    inlines = [VersionInline, ]


class ElemInlines(admin.StackedInline):
    model = ManualElem
    extra = 1


@admin.register(ManualVersion)
class ManualVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'manual_info', 'version', 'from_date')
    list_filter = ('manual_info', 'from_date', )
    inlines = [ElemInlines, ]


@admin.register(ManualElem)
class ManualElemAdmin(admin.ModelAdmin):
    list_display = ('manual', 'code', 'value')
    list_filter = ('manual', 'code')
