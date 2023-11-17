from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from product import models


class EditLinkInLine:
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )
        if instance.pk:
            link = mark_safe(f'<a href="{url}">edit</a>'.format(u=url))
            return link
        return ""


class ProductImageInLine(admin.TabularInline):
    model = models.ProductImage


class ProductLineInLine(EditLinkInLine, admin.TabularInline):
    model = models.ProductLine
    readonly_fields = ("edit",)


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductLineInLine,
    ]


class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageInLine]


admin.site.register(models.ProductLine, ProductLineAdmin)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category)
admin.site.register(models.Brand)
