from django.contrib import admin
from .models import Category, Product


@admin.action(description='Reset quantity to 0')
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """List of products."""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Single product."""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Product category and its detailed description',
                'fields': ['category', 'description']
            }
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity']
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                'fields': ['rating', 'date_added'],

            }
        ),
    ]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
