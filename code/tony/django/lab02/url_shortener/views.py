import random
from django.shortcuts import redirect
from django.views import generic

from .models import Url


class IndexView(generic.CreateView):
    model = Url
    fields = ['longurl']
    object = None # I don't know why I have to initialize this.

    def get(self, request, *args, **kwargs):
        """Display the newly created link in the view context."""
        link = request.GET.get("sc")
        if link:
            self.extra_context = {'link': f'/{link}'}
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        """TODO: I want to add URL formatting validation here, 
        and maybe even check the URL is responsive and accessible."""
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """Modify the shortcode value before saving."""
        form.instance.shortcode = get_str(1073741824)
        self.success_url = f'/?sc={form.instance.shortcode}'
        return super().form_valid(form)


class RedirectView(generic.View):
    def get(self, request, *args, **kwargs):

        url = Url.objects.get(shortcode=self.kwargs.get('sc')).longurl
        return redirect(url)


def get_base(x, ct=0):
    """Determine the proper string length for base64."""
    n = 64
    if x < n:
        return ct
    ct += 1
    return get_base(int(x / n) + int(x % n), ct=ct)


def get_str(the_id, min_length=5):
    """Get a base64 string that tries to match a complexity 
    based upon the amount of database entries."""

    b64 = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_')
    "There's probably a more pythonic way to get this list, but I don't know how to do it."
    return ''.join(b64[random.randint(0, 63)]
                   for _ in range(get_base(the_id) + min_length))
