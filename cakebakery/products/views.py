import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from .models import cake_list

stripe.api_key = settings.STRIPE_SECRET_KEY





class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['id']
        product = cake_list.objects.get(id = product_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'inr',
                        'unit_amount': product.price*100,
                        'product_data': {
                            'name': product.name ,
                            # 'images': ['https://www.facebook.com/106681217831349/photos/106683907831080/'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment-successfull/',
            cancel_url=YOUR_DOMAIN + '/payment-cancelled/',
        )
        return JsonResponse({
            'id' : checkout_session.id
        })
