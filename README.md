<h1> Решение тестового задания "Сервис по рассылке сообщений" </h1>

## Тестовое задание:

### Необходимо разработать сервис управления рассылками API администрирования и получения статистики.

```
Необходимо реализовать методы создания новой рассылки, просмотра созданных и получения статистики по выполненным рассылкам.
```

```
Реализовать сам сервис отправки уведомлений на внешнее API.
```

```
Опционально вы можете выбрать любое количество дополнительных пунктов описанных после основного.
```

```
Для успешного принятия задания как выполненного достаточно корректной и рабочей реализации требований по основной части, но дополнительные пункты помогут вам продемонстрировать ваши навыки в смежных технологиях.
```

## Детали реализации:

### Задача решена с помощью связки DRF + JS

### Реализован пользовательский UI на главной странице с возможность создать новую рассылку по критериям оператор (Билай, МТС, Мегафон) и Тэг(премиум, эконом, лайт). Рассылки выводятся в таблице (DataTables). По каждой выполненной рассылке доступна статистика с интегральными показателями число сообщений/число успешных сообщений и таблица с результатом отправки по каждому телефону в рассылке. Реализована возможность удаления рассылки.

### Документация(swagger) к проекту находится по адресу http://127.0.0.1:8000/docs/

### Реализовано логирование рассылки (по каждому сообщению и результат рассылки, доступность внешнего API и др.)

### При создании рассылки с прошедшей датой старта она начинается сразу же после рассылки (при условии что дата окончания правее текущей даты). Обновление статуса рассылки на главной странице можно увидеть путем обновления страницы через некоторое время после создания рассылки.

# Как установить проект

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AKafer/Test-task-Mailing.git
cd Test-task-Mailing/
```

### Создать и активировать виртуальное окружение:

```
python -m venv venv
source venv/Scripts/activate
```

### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Выполнить миграции и загрузить тестовые данные в БД:

```
cd application
python manage.py migrate
python manage.py loaddata data.json
```

### Запустить API проекта:

```
python manage.py runserver
```

### В новом терминале запустить программу рассылки (файл находится по адресу application/mailing/management/commands/send_mes.py):

```
source venv/Scripts/activate
cd application
python manage.py send_mes.py
```

## Стек технологий: Python 3, Django 4.1, DRF, JS, jQuery, DataTables

## Автор проекта - Сергей Сторожук

## Примечания:

```
1. В данной реализации рассылка выполняется в синхронном режиме. Увеличить скорость рассылки возможно с использованием многопоточности.
2. В пользовательском интерфейсе реализован минимальный объем проверок заполнения полей. Для корректной работы приложения необходимо заполнение всех полей в форме создания.
3. В таблице для каждой рассылки указываются телефоны, но возможно более оптимальным вариантом будет указание фильтров, использоваонных при создании рассылки.
```
