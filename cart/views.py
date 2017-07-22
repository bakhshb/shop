from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from catalogues.models import Product
from .forms import CartAddProductForm
from .cart import Cart 
from coupons.forms import CouponApplyForm
from catalogues.recommender import Recommender

class CartAdd (View):
	def post (self, request, *args, **kwargs):
		product_id = kwargs['product_id']
		cart = Cart(request)
		product = get_object_or_404(Product, id = product_id)
		form = CartAddProductForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			cart.add(product = product,
						quantity= cd['quantity'],
						update_quantity=cd['update'])
		return redirect ('cart:cart_detail')


class CartRemove(View):
	def get(self,request,*args, **kwargs):
		product_id = kwargs['product_id']
		cart= Cart(request)
		product = get_object_or_404(Product, id = product_id)
		cart.remove(product)
		return redirect('cart:cart_detail')

class CartDetail (View):
	def get (self,request,*args, **kwargs):
		cart= Cart(request)
		if cart:
			for item in cart:
				item['update_quantity_form'] = CartAddProductForm(initial={'qunatity':item['quantity'],
																			'update':True})
			coupon_apply_form = CouponApplyForm()
			
			r = Recommender()
			car_products = [item['product'] for item in cart]
			if car_products:
				recommended_products = r.suggest_products_for (car_products,4)
				return render(request,'cart/detail.html',{'cart':cart,
														'coupon_apply_form':coupon_apply_form,
														'recommended_products':recommended_products})
			else:
				return render(request,'cart/detail.html',{'cart':cart,
														'coupon_apply_form':coupon_apply_form})
		else:
			return redirect ('shop:product_list')