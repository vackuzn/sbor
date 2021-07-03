from main.models import SiteSettings


def main(request):
    init_settings()

    context = {
        'min_sum': int(SiteSettings.objects.get(key_title='min_sum').value),
        'contacts_telephone': SiteSettings.objects.get(key_title='contacts_telephone').value,
        'contacts_time': SiteSettings.objects.get(key_title='contacts_time').value,
        'contacts_email': SiteSettings.objects.get(key_title='contacts_email').value,
        'contacts_for_order': SiteSettings.objects.get(key_title='contacts_for_order').value,
    }
    return context


def init_settings():
    if SiteSettings.objects.count() > 0:
        return

    default_settings = [
        SiteSettings(key_title="min_sum", description="Минимальная сумма заказа", value="1200"),
        SiteSettings(key_title="contacts_telephone", description="Телефон в шапке сайта", value="+79817363599"),
        SiteSettings(key_title="contacts_time", description="Время работы в шапке сайта",
                     value="Доставка ежедневно с 9:00 до 21:00"),
        SiteSettings(key_title="contacts_email", description="Адрес электронной почты в шапке сайта",
                     value="sbor-market@mail.ru"),
        SiteSettings(key_title="contacts_for_order", description="Телефон в случае отсутствия товара на складе",
                     value="+7 981 736 3599"),
    ]

    for setting in default_settings:
        setting.save()
