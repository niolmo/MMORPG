from celery import shared_task
from django.contrib.auth.models import User
from .models import Ads, Response
from django.core.mail import send_mail
from datetime import timedelta
from django.utils import timezone


@shared_task
def respond_send_email(respond_id):
    respond = Response.objects.get(id=respond_id)
    send_mail(
        subject=f'MMORPG Billboard: новый отклик на объявление!',
        message=f'Здравствуйте!, {respond.post.author}, ! На ваше объявление откликнулись!\n'
                f'Прочитать:\nhttp://127.0.0.1:8000/responses/{respond.post.id}',
        from_email='test.niolmo@yandex.ru',
        recipient_list=[respond.post.player.email, ],
    )


@shared_task
def respond_accept_send_email(response_id):
    respond = Response.objects.get(id=response_id)
    print(respond.post.author.email)
    send_mail(
        subject=f'MMORPG Billboard: Ваш отклик принят!',
        message=f'Автор объявления {respond.post.title} принял Ваш отклик!\n'
                f'Посмотреть принятые отклики:\nhttp://127.0.0.1:8000/responses',
        from_email='test.niolmo@yandex.ru',
        recipient_list=[respond.post.player.email, ],
    )


@shared_task
def send_mail_monday_8am():
    # Создаем список всех объявлений, созданных за последние 7 дней (list_week_posts)
    now = timezone.now()
    list_week_posts = list(Ads.objects.filter(
        dateCreation__gte=now - timedelta(days=7)))
    if list_week_posts:
        for user in User.objects.filter():
            print(user)
            list_posts = ''
            for post in list_week_posts:
                list_posts += f'\n{post.title}\nhttp://127.0.0.1:8000/post/{post.id}'
            send_mail(
                subject=f'News Portal: посты за прошедшую неделю.',
                message=f'Здравствуйте!, {user.username}!\nЭто объявления, '
                        f'появившиеся за последние 7 дней:\n{list_posts}',
                from_email='test.niolmo@yandex.ru',
                recipient_list=[user.email, ],
            )
