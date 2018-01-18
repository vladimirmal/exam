
from django import forms
from django.contrib import admin
from exam_app.models import Categories, Products, ProductVersion
from django.core.urlresolvers import reverse


class VersionProductForm(forms.ModelForm):
    class Meta:
        model = ProductVersion
        exclude = ()


class VersionProduct(admin.ModelAdmin):
    form = VersionProductForm
    list_display = ('title', 'description', 'base_product', 'cost')
    search_fields = ('title',) and ('base_product',) and ('cost',)

    def get_products(self, obj):
        link = reverse('admin:exam_shop_product_change', args=[obj.version.id])
        return '<a href="{}">{}</a>'.format(link, obj.version.title)
    get_products.admin_order_field = 'version__title'
    get_products.short_description = 'Version title'
    get_products.allow_tags = True


class CategoryCreatedForm(forms.ModelForm):

    class Meta:
        model = Categories
        exclude = ()


class CategoriesCreated(admin.ModelAdmin):
    form = CategoryCreatedForm
    list_display = ('title', 'created_at', 'updated_at', )
    readonly_fields = ('updated_at', 'created_at', )


class ProductsCreatedForm(forms.ModelForm):

    class Meta:
        model = Products
        exclude = ()


class ProductsCreated(admin.ModelAdmin):
    form = ProductsCreatedForm
    list_display = ('title', 'category')


    def get_categories(self, obj):
        link = reverse('admin:exam_shop_product_change', args=[obj.product.id])
        return '<a href="{}">{}</a>'.format(link, obj.product.title)
    get_categories.admin_order_field = 'product__title'
    get_categories.short_description = 'Product title'
    get_categories.allow_tags = True


admin.site.register(Categories, CategoriesCreated)
admin.site.register(Products, ProductsCreated)
admin.site.register(ProductVersion, VersionProduct)

# Register your models here.
