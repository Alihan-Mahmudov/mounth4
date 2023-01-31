from django.shortcuts import render, redirect
from products.models import Product, Comment
from products.forms import ProductCreateView, CommentCreateView

# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()


        context = {
            'products': products,
            'user': request.user
        }


        return render(request, 'products/products.html', context = context)


def product_detail_view(request, id):
    if request.method =='GET':
        product_obj = Product.objects.get(id=id)
        comments = Comment.objects

        context = {
            'product': product_obj,
            'comments': comments,
            'form': CommentCreateView
        }


        return render(request, 'products/detail.html',context = context)

    if request.method == 'POST':
        product_obj = Product.objects.get(id=id)
        comments = Comment.objects
        form = CommentCreateView(data=request.POST)

        if form.is_valid():
            Comment.objects.create(
                post=product_obj,
                text=form.cleaned_data.get('text')
            )

            return redirect(f'/products/{product_obj.id}/')
        return render(request, 'products/detail.html', context={
            'product': product_obj,
            'comments': comments,
            'form': form
        })

def create_product_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateView
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateView(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data['rate'] if form.cleaned_data['rate'] is not None else 5,
            )
            return redirect('/products/')
