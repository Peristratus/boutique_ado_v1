from django.shortcuts import render


def profile(request):
    """ Dispaly the users Profile. """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)


