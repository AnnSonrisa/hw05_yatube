# Описание проекта Yatube.
Yatube - это социальная сеть блогеров. 

В проекте реализованы следующие функции:

 - Создание сообщества для публикаций.
 - Публикация поста в ленте, (возможность выбора группы, в которой появится этот пост);
 - Добавление новых записей авторизованными пользователями;
 - Добавление фотографий;
 - Добавление и редактирование комментариев;
 - Редактирование постов только его автором;
 - Подписка/отписка на авторов;
 - Создание отдельной ленты с постами авторов на которых подписан пользователь;
 - Реализовано кэширование, работает на главной странице;
 - Работает пагинация;

## Как запустить проект:
1) Клонировать репозиторий и перейти в него в командной строке:
`git clone https://github.com/AnnSonrisa/hw05_yatube.git`

2) Cоздать и активировать виртуальное окружение:
`python -m venv venv`

`source venv/Scripts/activate`

3) Установить зависимости из файла requirements.txt:
`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

4) Выполнить миграции:
`python3 manage.py migrate`
