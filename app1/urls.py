from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_home_page_function, name="main_home_page_function"),
    path('main_login', views.main_login_function, name="main_login_function"),
    path('about_us_readmore', views.about_us_readmore_function, name="about_us_readmore_function"),
    path('about_us_readmore1', views.about_us_readmore1_function, name="about_us_readmore1_function"),
    path('goto_main_home_page', views.goto_main_home_page_function, name="goto_main_home_page_function"),





    # Home Page return
    # ----------------
    path('back_to_homepage', views.back_to_homepage_function, name="back_to_homepage_function"),
    path('seller_homepage_return', views.seller_homepage_return_function, name="seller_homepage_return_function"),
    path('seller_homepage_return_1', views.seller_homepage_return_1_function, name="seller_homepage_return_1_function"),
    path('seller_profile_redirect', views.seller_profile_redirect_function, name="seller_profile_redirect_function"),




    # Admin Functions
    # ----------------
    path('admin_home', views.admin_home_function, name="admin_home_function"),
    path('admin_view_all_products', views.admin_view_all_products_function, name="admin_view_all_products_function"),
    path('admin_delete_product/<int:g>', views.admin_delete_product_function, name="admin_delete_product_function"),
    path('admin_view_all_images/<int:h>', views.admin_view_all_images_function, name="admin_view_all_images_function"),
    path('admin_view_all_seller_personal_details', views.admin_view_all_seller_personal_details_function, name="admin_view_all_seller_personal_details_function"),
    path('admin_rejected_products', views.admin_rejected_products_function, name="admin_rejected_products_function"),
    path('admin_view_rejected_seller_details/<int:i>', views.admin_view_rejected_seller_details_function, name="admin_view_rejected_seller_details_function"),
    path('admin_delete_account_of_seller', views.admin_delete_account_of_seller_function, name="admin_delete_account_of_seller_function"),
    path('admin_delete_seller_account/<int:j>', views.admin_delete_seller_account_function, name="admin_delete_seller_account_function"),
    path('admin_view_admin_deleted_seller_accounts', views.admin_view_admin_deleted_seller_accounts_function, name="admin_view_admin_deleted_seller_accounts_function"),
    path('control_comments', views.control_comments_function, name="control_comments_function"),
    path('admin_delete_comment/<int:o>', views.admin_delete_comment_function, name="admin_delete_comment_function"),
    path('admin_view_all_transaction', views.admin_view_all_transaction_function, name="admin_view_all_transaction_function"),
    path('admin_view_all_transaction_details/<int:r>', views.admin_view_all_transaction_details_function, name="admin_view_all_transaction_details_function"),
    path('admin_view_buyers_detail', views.admin_view_buyers_detail_function, name="admin_view_buyers_detail_function"),
    path('admin_view_buyer_products/<int:r>', views.admin_view_buyer_products_function, name="admin_view_buyer_products_function"),
    path('admin_del_buyer_account/<int:s>', views.admin_del_buyer_account_function, name="admin_del_buyer_account_function"),


    # User registration
    # -----------------
    path('user_registration', views.seller_registration_function, name="seller_registration_function"),

    # Seller product uploading
    # ------------------------
    path('seller_home', views.seller_home_function, name="seller_home_function"),
    path('sell_product', views.sell_product_function, name="sell_product_function"),
    path('seller_personal_data/<int:a>', views.seller_personal_data_function, name="seller_personal_data_function"),
    path('seller_personal_data_update/<int:b>', views.seller_personal_data_update_function, name="seller_personal_data_update_function"),
    path('seller_products/<int:c>', views.seller_product_function, name="seller_product_function"),

    # Seller Edit Profile
    # -------------------
    path('seller_delete_products/<int:d>', views.seller_delete_products_function, name="seller_delete_products_function"),
    path('seller_view_all_images/<int:e>', views.seller_view_all_images_function, name="seller_view_all_images_function"),
    path('seller_edit_image_details/<int:f>', views.seller_edit_image_details, name="seller_edit_image_details"),
    path('seller_transactions', views.seller_transactions_function, name="seller_transactions_function"),
    path('seller_view_transaction_history_individual/<int:q>', views.seller_view_transaction_history_individual_function, name="seller_view_transaction_history_individual_function"),
    path('seller_transaction_go_back_button', views.seller_transaction_go_back_button_function, name="seller_transaction_go_back_button_function"),
    path('about_us_deadmore_guideline', views.about_us_deadmore_guideline_function, name="about_us_deadmore_guideline_function"),


    # Stranger at homepage
    # --------------------
    path('login_for_buy_product/<int:k>', views.login_for_buy_product_function, name="login_for_buy_product_function"),
    path('redirect_to_login_page/<int:m>', views.redirect_to_login_page_function, name="redirect_to_login_page_function"),
    path('redirect_to_buyer_registration', views.redirect_to_buyer_registration_function, name="redirect_to_buyer_registration_function"),

    # Buyer Registration
    # -------------------
    path('buyer_registration', views.buyer_registration_function, name="buyer_registration_function"),

    # Login for buyer
    # ----------------
    path('buyer_home_page', views.buyer_home_function, name="buyer_home_function"),
    path('buyer_return_homepage', views.buyer_return_homepage_function, name="buyer_return_homepage_function"),
    path('buyer_personal_details/<int:l>', views.buyer_personal_details_function, name="buyer_personal_details_function"),
    path('buyer_home_buy_button/<int:n>', views.buyer_home_buy_button_function, name="buyer_home_buy_button_function"),
    path('Buyer_transactions', views.Buyer_transactions_function, name="Buyer_transactions_function"),
    path('buyer_transaction_individual_item_full_details/<int:p>', views.buyer_transaction_individual_item_full_details_function, name="buyer_transaction_individual_item_full_details_function"),
    path('buyer_goback_button_to_all_transaction', views.buyer_goback_button_to_all_transaction_function, name="buyer_goback_button_to_all_transaction_function"),


    # Invoice generation after payment success
    # ----------------------------------------
    path('buyer_home_page/success/', views.success, name="success"),

    # Search Products
    # ---------------
    path('search', views.search_function, name="search_function"),

    # Buyer Search Products
    # ---------------------
    path('buyer_search', views.buyer_search_function, name="buyer_search_function"),

    # Comments
    # --------
    path('all_comments', views.all_comments_function, name="all_comments_function"),




    # Logouts
    # -------
    path('buyer_logout', views.buyer_logout_function, name="buyer_logout_function"),
    path('seller_logout', views.seller_logout_function, name="seller_logout_function"),
    path('admin_logout', views.admin_logout_function, name="admin_logout_function")

]