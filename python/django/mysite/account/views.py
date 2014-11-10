from django.shortcuts import render, render_to_response
from django.template import RequestContext
from account.forms import UserForm, UserProfileForm

# Create your views here.


def register(request):
    # Like before,get the request's context.
    context = RequestContext(request)

    registered = False

    if request.mothod == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # two forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            # save the user's form data to the database
            user = user_form.save()

            # hash the password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # save UserProfile model instance
            profile.save()

            registered = True

        # invalid forms,
        else:
            print user_form.errors, profile_form.errors

    # not a http post
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context
    return render_to_response(
        'account/register.html',
        {'user_form': user_form,
         'profile_form': profile_form,
         'registered': registered},
        context
    )
