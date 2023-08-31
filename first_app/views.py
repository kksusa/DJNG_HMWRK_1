from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def text(title, any_text):
    return f'<h2>{title}</h2>' \
           f'<p>{any_text}</p>'


def general(request):
    title = 'Главная страница'
    body_text = 'Главная страница сайта с информацией.'
    logger.info('General page')
    return HttpResponse(text(title, body_text))


def about(request):
    title = 'Страница о себе'
    body_text = 'Я учусь на платформе Geekbrains<br>' \
                'Специализация - Программист Python'
    logger.info('About page')
    return HttpResponse(text(title, body_text))
