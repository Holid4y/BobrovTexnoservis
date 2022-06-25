from django.db import models

class staff(models.Model):
    last_name = models.CharField('Фамилия', max_length=40)
    first_name = models.CharField('Имя', max_length=40)
    patronymic = models.CharField('Отчество', max_length=40)
    phone = models.CharField('Телефон', max_length=20)
    email = models.CharField('E-mail', max_length=100)
    post = models.TextField('Должность')
    date = models.DateField('Дата найма')
    def __str__(self):
        return self.last_name + " " + self.first_name + " " + self.patronymic
    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Сотрудники'

class news(models.Model):
    title = models.CharField('Название новости', max_length=40)
    text = models.TextField('Текст новости')
    date = models.DateField('Дата публикации')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class record(models.Model):
    FIO = models.CharField('ФИО', max_length=100)
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    def __str__(self):
        return self.FIO
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

class message(models.Model):
    FirstName = models.CharField('Имя', max_length=100)
    Phone = models.CharField('Телефон', max_length=50)
    Email = models.CharField('E-mail', max_length=100)
    Message = models.TextField('Сообщение')
    Checkbox = models.BooleanField('Обработка данных')
    def __str__(self):
        return f'Сообщение: {self.FirstName}, {self.Phone}, {self.Email}'
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'