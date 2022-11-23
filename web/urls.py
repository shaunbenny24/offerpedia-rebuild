from django.urls import path
from . import views



urlpatterns = [

    path('', views.public_index, name='public_index'),
    path('business', views.public_business, name='public_business'),

    path('campaigns/', views.public_campaigns, name='public_campaigns'),
    path('campaign/', views.campaign_view, name='campaign_view'),



    path('profile', views.profile, name='profile'),


#     path('send-otp/, views.send_otp', name='send_otp'),
#     path('resend-otp/, views.resend_otp', name='resend_otp'),

#     path('contact-us', views.contact_us, name='contact_us'),
#     path('privacies', views.privacy, name='privacy'),
#     path('supports', views.support, name='support'),
    path('privacy', views.public_privacy, name='public_privacy'),
    path('support', views.public_support, name='public_support'),

#     path('submit-cashback/',
#         views.submit_cashback, name='submit_cashback'),
#     path('submit-voucher/',
#         views.submit_voucher, name='submit_voucher'),
#     path('submit-bill-amount-cashback/',
#         views.submit_bill_amount_cashback, name='submit_bill_amount_cashback'),

#     path('rewards', views.rewards, name='rewards'),
#     path('reward-request/',
#         views.reward_request, name='reward_request'),
#     path('reward-admin-approved/',
#         views.reward_admin_approved, name='reward_admin_approved'),
#     path('reward-withdraw-reward/',
#         views.withdraw_reward, name='withdraw_reward'),

#     path('product-details/', views.product_details, name='product_details'),
#     path('products', views.products_related_category, name='products_related_category'),
#     path('frequently-asked-questions', views.faq, name='faq'),
#     path('active-campaigns', views.ecommerce_active_campaigns, name='ecommerce_active_campaigns'),
#     path('cart', views.anonymous_user_cart, name='anonymous_user_cart'),
#     path('cart-details', views.take_cart_details, name='take_cart_details'),
#     path('user-cart-details', views.take_user_cart_details, name='take_user_cart_details'),
#     path('my-account', views.my_profile, name='my_profile'),
#     path('cart-restart', views.user_cart_restart, name='user_cart_restart'),
#     path('add-cashback-amount', views.add_cashback_amount, name='add_cashback_amount'),
#     path('social-share-link/', views.social_share_link, name='social_share_link'),

#     path('export-products/', views.export_products, name='export_products'),
#     path('export-orders', views.export_orders, name='export_orders'),

#     path('location-autocomplete',views.LocationAutocomplete.as_view(),name='location_autocomplete'),
#     path('create-location/', views.create_delivery_location, name="create_delivery_location"),
#     path('locations/', views.delivery_locations, name="delivery_locations"),
#     path('view-location/', views.delivery_location, name="delivery_location"),
#     path('edit-location/', views.edit_delivery_location, name="edit_delivery_location"),
#     path('delete-location/', views.delete_delivery_location, name="delete_delivery_location"),
#   	path('delete-selected-location',views.delete_selected_locations , name='delete_selected_locations'),

 ]
