from django.contrib.auth.decorators import user_passes_test

def admin_or_staff_required(view_func):

    def test_func(user):
        return user.is_staff or user.is_superuser

    return user_passes_test(test_func, login_url='login')(view_func)