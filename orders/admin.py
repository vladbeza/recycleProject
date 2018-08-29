import csv
import datetime

from django.contrib import admin
from .models import Order, OrderItem
from django.http import HttpResponse

from django.shortcuts import reverse
from django.utils.html import format_html


def export_to_CSV(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; \
        filename=Orders-{}.csv'.format(datetime.datetime.now().strftime("%d/%m/%Y"))
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])

    for obj in queryset:
        row = []
        for f in fields:
            value = getattr(obj, f.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            row.append(value)
        writer.writerow(row)

    return response
    export_to_CSV.short_description = "Export CSV"


def order_detail(obj):
    return format_html('<a href="{}">Watch</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])
    ))

def order_pdf(obj):
    return format_html('<a href="{}">PDF</a>'.format(
        reverse('orders:admin_order_pdf', args=[obj.id])
    ))
order_pdf.short_description = 'To PDF'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_field = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", "address", "city", "created", "updated", "paid",
                    order_detail, order_pdf]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
    actions = [export_to_CSV]

admin.site.register(Order, OrderAdmin)