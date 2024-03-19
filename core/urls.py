from django.urls import path
from core.views import (
    index,
    account_view,
    index_view,
    product_view,
    cart_view,
    explore_view,
    anaant_view,
    kathua_view,
    anantnag_view,
    budgam_view,
    jammu_view,
    rajouri_view,
    srinagar_view,
    shopian_view,
    baramulla_view,
)

app_name = "core"

urlpatterns = [
    path("", index, name="index"),
    path("user/sign", account_view, name="sign-up"),
    path("product", product_view, name="products"),
    path("cart", cart_view, name="cart"),
    path("explore", explore_view, name="explore"),
    path("anaant", anaant_view, name="anaant"),
    path("kathua", kathua_view, name="kathua"),
    path("anantnag", anantnag_view, name="anantnag"),
    path("budgam", budgam_view, name="budgam"),
    path("jammu", jammu_view, name="jammu"),
    path("rajouri", rajouri_view, name="rajouri"),
    path("srinagar", srinagar_view, name="srinagar"),
    path("shopian", shopian_view, name="shopian"),
    path("baramulla", baramulla_view, name="baramulla"),

]
