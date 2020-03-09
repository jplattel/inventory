from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from organization.models.inventory import Product, Location, Mutation
from django.db.models import Sum, Value

@login_required
def reports_index(request):
    products = Product.objects.for_organization(request.organization)
    return render(request, "reports/index.html", {
        "counts": {
            "products": products.count(),
            "locations": Location.objects.for_organization(request.organization).count(),
            "mutations": Mutation.objects.for_organization(request.organization).count(),
            "users": request.organization.users.count(),
        },
        "products": {
            "total_price_cost": sum(product.data.get('sum_price_cost', 0) for product in products),
            "total_price_sale": sum(product.data.get('sum_price_sale', 0) for product in products),
            "total_profit": sum(product.data.get('sum_profit', 0) for product in products)
        }
    })
