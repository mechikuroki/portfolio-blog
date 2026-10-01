from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Product, Comment
from .forms import ProductForm, CommentForm  

def product_list(request):
    products = Product.objects.all()
    return render(request, 'blogsite/blog.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            
            parent_id = request.POST.get('parent_id')
            if parent_id:
                try:
                    parent_comment = Comment.objects.get(pk=parent_id)
                    comment.parent = parent_comment
                except Comment.DoesNotExist:
                    pass 
            
            comment.save()
            send_mail(
                subject='Welcome to Our Platform!',
                message="This is the plain-text fallback message for email clients that don't support HTML.",
                from_email=None,
                recipient_list=[form.cleaned_data['email']],
                html_message="<h1>Hello!</h1><p>This is an <strong>HTML</strong> formatted email.</p>",
                fail_silently=False
                )
            return redirect('product_detail', pk=pk)
    else:
        form = CommentForm()

    comments = product.comments.filter(parent__isnull=True)
    return render(request, 'blogsite/blog2.html', {'product': product,
                                           'comments': comments,
                                           'comment_form': form})

'''
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
            return redirect('product_detail', pk=pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blogsite/blog2.html', {'product': product,
                                           'comments': product.comments,
                                           'comment_form': comment_form})
'''

def search(request):
    if request.method == 'POST':
        products = Product.objects.none()
        search_text = request.POST.get('search_query', '') 
        
        if 'search_products' in request.POST:
            products = Product.objects.filter(name__icontains=search_text).distinct()
            
        elif 'search_tags' in request.POST:
            products = Product.objects.filter(tags__name__icontains=search_text).distinct()
            
        return render(request, 'blogsite/blog.html', {'products': products})

    else:
        return redirect('product_list')

def delete(request, pk):
    if request.user.is_superuser:
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            product.delete()
            return redirect('product_list')
        return render(request, 'blogsite/delete.html', {'product': product})
    else:
        return redirect('product_list')

def delete_comment(request, pk):
    if request.user.is_superuser:
        comment = get_object_or_404(Comment, pk=pk)
        if request.method == 'POST':
            comment.delete()
            return redirect('product_list')
        return render(request, 'blogsite/delete_comment.html', {'comment': comment})
    else:
        return redirect('product_list')

    
"""
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if r|equest.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'blogsite/edit.html', {'form': form})


def home(request):
    return HttpResponse('Hello, World!')

"""

