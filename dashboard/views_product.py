from django.contrib import messages
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from dashboard.forms import ProductForm
from dashboard.models import Inventory, Mutation, Product


def products(request):
    return render(
        request, "dashboard/products.html", {"products": Product.objects.all()}
    )


def product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    inventories = Inventory.objects.filter(amount__gt=0, product=product)
    product_total = Inventory.objects.filter(product=product).aggregate(Sum("amount"))
    mutations = Mutation.objects.filter(product=product).order_by("-created")
    return render(
        request,
        "dashboard/product/view.html",
        {
            "product_total": product_total,
            "product": product,
            "inventories": inventories,
            "mutations": mutations,
        },
    )


def product_form(request, product_id=None):
    # Creating a new product..
    if request.method == "POST" and product_id == None:
        form = ProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Product created!")
            return redirect("products")

    # Deleting a product
    elif (
        request.method == "POST"
        and product_id
        and request.POST.get("action") == "delete"
    ):
        instance = get_object_or_404(Product, id=product_id)
        instance.delete()
        messages.add_message(request, messages.INFO, "Product deleted!")
        return redirect("products")

    # Updating a product
    elif request.method == "POST" and product_id != None:
        instance = get_object_or_404(Product, id=product_id)
        form = ProductForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Product updated!")
            return redirect("products")

    # Otherwise: get form
    elif product_id:
        instance = get_object_or_404(Product, id=product_id)
        form = ProductForm(instance=instance)
        return render(request, "dashboard/product/form.html", {"form": form})

    else:
        form = ProductForm()
        return render(request, "dashboard/product/form.html", {"form": form})
