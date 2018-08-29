from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Cupon
from .form import CuponForm

@require_POST
def cupon_apply(request):
    now = timezone.now()
    form = CuponForm(request.POST)
    if form.is_valid():
        try:
            code = form.cleaned_data["code"]
            cupon = Cupon.objects.get(code__iexact = code,
                                           active_from__lte = now,
                                           active_to__gte = now,
                                           is_active = True)
            request.session["cupon_id"] = cupon.id
        except Cupon.DoesNotExist:
            request.session["cupon_id"] = None

    return redirect("cart:cart_detail")

