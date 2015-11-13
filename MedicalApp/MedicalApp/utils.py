from functools import wraps

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.decorators import available_attrs


def user_passes_test_with_kwargs(test_func):
    """
    Decorator for views that checks that the user passes the given test,
    redirecting to the log-in page if necessary. The test should be a callable
    that takes the user object and returns True if the user passes.
    --------------------------------------------------------------------------
    Modified so that test_func in user_passes_test takes additional arguments
    and if the test fails, redirects the user to specified url
    """

    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if test_func(request.user, **kwargs):
                return view_func(request, *args, **kwargs)

            return redirect(reverse('403'))
        return _wrapped_view
    return decorator
