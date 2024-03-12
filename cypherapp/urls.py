from django.urls import path

from django.contrib.auth import views as auth_views

from django.conf import settings

from . import views

urlpatterns=[

	path('', views.home, name='home'),

	path('plan/', views.plan, name='plan'),

	path('otherpayment/', views.otherpayment, name='otherpayment'),

	path('about/', views.about, name='about'),

	path('career/', views.career, name='career'),

	path('signin/', views.signin, name='signin'),

	path('privacy/', views.privacy, name='privacy'),

	path('main-view/', views.main_view, name='main-view'),

	path('main-view/<str:ref_code>/', views.main_view, name='main-view'),

	path('signup/', views.signup, name='signup'),

	path('terms/', views.terms, name='terms'),

	path('refund/', views.refund, name='refund'),

	path('Nft/', views.Nft, name='Nft'),

	path('cryptography/', views.cryptography, name='cryptography'),

	path('blockchaindevelopment/', views.blockchaindevelopment, name='blockchaindevelopment'),

	path('Dao/', views.Dao, name='Dao'),

	path('contact/', views.contact, name='contact'),

	path('stocks/', views.stocks, name='stocks'),

	path('smartcontract/', views.smartcontract, name='smartcontract'),

	path('defi/', views.defi, name='defi'),

	path('cybersecurity/', views.cybersecurity, name='cybersecurity'),

	path('dashboard/', views.dashboard, name='dashboard'),

	path('admindashboard/', views.admindashboard, name="admindashboard"),

	path('deposit/', views.deposit, name='deposit'),

	path('withdrawal/', views.withdrawal, name='withdrawal'),

	path('history/', views.history, name='history'),

	path('pending_deposit/', views.pending_deposit, name='pending_deposit'),

	path('pending_withdrawal/', views.pending_withdrawal, name='pending_withdrawal'),

	path('pending_bonus/', views.pending_bonus, name='pending_bonus'),

	path('completed_transaction/', views.completed_transaction, name='completed_transaction'),

	path('myreferals/', views.myreferals, name='myreferals'),

	path('confirm_withdrawal/', views.confirm_withdrawal, name='confirm_withdrawal' ),

	path('update_withdrawal/<str:pk>/', views.update_withdrawal, name='update_withdrawal' ),

	path('decline_wihdrawal/<str:pk>/', views.decline_wihdrawal, name='decline_wihdrawal'),

	path('confirm_deposit/', views.confirm_deposit, name='confirm_deposit' ),

	path('update_payment/<str:pk>/', views.update_payment, name='update_payment' ),

	path('account_settings/', views.account_settings, name='account_settings'),

	path('create_bonus/', views.create_bonus, name='create_bonus'),

	path('use_bonus/', views.use_bonus, name='use_bonus'),

	path('reset_password/', auth_views.PasswordResetView.as_view(template_name="cypherapp/password_reset.html"), name='reset_password'),

	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="cypherapp/password_reset_done.html"), name='password_reset_done'),

	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="cypherapp/password_reset_form.html"), name='password_reset_confirm'),

	path('reset_password_complete/', auth_views.PasswordResetView.as_view(template_name="cypherapp/password_reset_complete.html"), name='password_reset_complete'),
	path('notifications/', views.notifications, name='notifications'),
	path('transfer_funds/', views.transfer_funds, name='transfer_funds'),
	path('video_page/', views.video_page, name='video_page'),
	path('reinvest/', views.reinvest, name='reinvest'),
	path('loan/', views.loan, name='loan'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('cybersecurityDeposit/', views.cybersecurityDeposit, name='cybersecurityDeposit'),
	path('NftDeposit/', views.NftDeposit, name='NftDeposit'),
	path('BlockchaindevelopmentDeposit/', views.BlockchaindevelopmentDeposit, name='BlockchaindevelopmentDeposit'),
	path('cryptographyDeposit/', views.cryptographyDeposit, name='cryptographyDeposit'),
	path('DaoDeposit/', views.DaoDeposit, name='DaoDeposit'),
	path('smartcontractDeposit/', views.smartcontractDeposit, name='smartcontractDeposit'),
	path('DefiDeposit/', views.DefiDeposit, name='DefiDeposit'),
	path('investmentPlans/', views.investmentPlans, name='investmentPlans'),
	path('logout/', views.logoutuser, name='logout'),
]