from functools import wraps

from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.utils.decorators import available_attrs
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin, ProcessFormView


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


# From https://gist.github.com/michelts/1029336#file-gistfile1-py-L6
class MultipleFormsMixin(FormMixin):
    """
    A mixin that provides a way to show and handle several forms in a
    request.
    """
    form_classes = {} # set the form classes as a mapping
    form_initial = {}

    def get_form_classes(self):
        return self.form_classes

    def get_initial(self):
        self.get_form_initial()
        initial = super(MultipleFormsMixin, self).get_initial()
        for key, klass in self.form_classes.items():
            if self.form_initial.get(key):
                initial[key] = model_to_dict(self.form_initial.get(key))

        return initial

    def get_forms(self, form_classes):
        form_initial = self.get_initial()
        return dict([(key, klass(initial=form_initial.get(key))) \
            for key, klass in form_classes.items()])

    def get_form(self, form_class=None):
       return None


    def get_forms_with_request(self, post_request, file_request, form_classes):
        return dict([(key, klass(post_request, file_request)) \
            for key, klass in form_classes.items()])

    def forms_valid(self, forms):
        for key, klass in self.form_classes.items():
            obj = klass(self.request.POST, self.request.FILES, instance=self.form_initial.get(key))
            obj.save()
        return super(MultipleFormsMixin, self).form_valid(forms)

    def forms_invalid(self, forms):
        return self.render_to_response(self.get_context_data(forms=forms))


class ProcessMultipleFormsView(ProcessFormView):
    """
    A mixin that processes multiple forms on POST. Every form must be
    valid.
    """
    def get(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        return self.render_to_response(self.get_context_data(forms=forms))

    def post(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        self.get_initial()
        forms = self.get_forms_with_request(request.POST, request.FILES, form_classes)
        if all([form.is_valid() for form in forms.values()]):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)


class BaseMultipleFormsView(MultipleFormsMixin, ProcessMultipleFormsView):
    """
    A base view for displaying several forms.
    """


class MultipleFormsView(TemplateResponseMixin, BaseMultipleFormsView):
    """
    A view for displaing several forms, and rendering a template response.
    """


