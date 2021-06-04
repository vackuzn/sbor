from main.models import SiteSettings


def main(request):
    context = {
        'min_sum': int(SiteSettings.objects.get(id=1).value),
        'contacts_telephone': SiteSettings.objects.get(key_title='contacts_telephone').value,
        'contacts_time': SiteSettings.objects.get(key_title='contacts_time').value,
        'contacts_email': SiteSettings.objects.get(key_title='contacts_email').value,
    }
    return context