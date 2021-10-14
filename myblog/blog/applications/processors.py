from applications.home.models import Home


def home_contact(request):
    home = Home.objects.latest('created')

    return {
        'phone': home.phone,
        'correo': home.contact_email,
    }
