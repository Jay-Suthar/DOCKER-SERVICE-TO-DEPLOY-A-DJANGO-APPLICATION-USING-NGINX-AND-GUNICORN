from .models import Item
from django.shortcuts import render, redirect
from django.views import View



class ItemListView(View):
    def get(self, request):
        items = Item.objects.all()
        return render(request, "item_list.html", {'items': items})


class AddItemView(View):
    def get(self, request):
        return render(request, "item_add.html")

    def post(self, request):
        name = request.POST.get("name")
        description = request.POST.get("description")
        count = request.POST.get("count")

        item = Item()
        item.name = name
        item.description = description
        item.count = count

        item.save()

        return redirect("item_list")
