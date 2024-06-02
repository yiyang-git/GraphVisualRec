from django.urls import path
from .views import AuthView, RegisterView, LogOut, AccountSet, DatausageStatistics, UserFeedbackView


urlpatterns = [
    path(
        "",
        AuthView.as_view(template_name="auth_login_basic.html"),
        name="auth-basic",
    ),
    path(
        "auth/login/",
        AuthView.as_view(template_name="auth_login_basic.html"),
        name="auth-login-basic",
    ),
    path(
        "auth/register/",
        RegisterView.as_view(template_name="auth_register_basic.html"),
        name="auth-register-basic",
    ),
    path(
        "auth/forgot_password/",
        AuthView.as_view(template_name="auth_forgot_password_basic.html"),
        name="auth-forgot-password-basic",
    ),
    path(
        "auth/logout/",
        LogOut.as_view(template_name="auth_forgot_password_basic.html"),
        name="logout",
    ),
    path(
        "auth/accountset/",
        AccountSet.as_view(template_name="auth_account_settings.html"),
        name="auth_account_settings",
    ),
    path(
        "auth/datausage_statistics/",
        DatausageStatistics.as_view(template_name="auth_datausage_statistics.html"),
        name="auth_datausage_statistics",
    ),
    path(
        "auth/user_feedback/",
        UserFeedbackView.as_view(template_name="auth_user_feedback.html"),
        name="auth_user_feedback",
    ),
]
