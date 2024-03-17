from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    """ Модель контакта """

    email = models.EmailField(verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=100, verbose_name='город', **NULLABLE)
    street = models.CharField(max_length=100, verbose_name='улица', **NULLABLE)
    house = models.CharField(max_length=100, verbose_name='номер дома', **NULLABLE)

    def __str__(self):
        return (f'{self.email}, адрес {self.country}, '
                f'г. {self.city}, ул. {self.street}, кв. {self.house}')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Product(models.Model):
    """ Модель продукта """

    name = models.CharField(max_length=100, verbose_name='название продукта')
    model = models.CharField(max_length=100, verbose_name='модель продукта', **NULLABLE)
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок', **NULLABLE)

    def __str__(self):
        return f'{self.name}, {self.model}, вышел на рынок {self.release_date}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Supplier(models.Model):
    """ Модель поставщика """

    FACTORY = '0'
    RETAIL_NETWORK = '1'
    INDIVIDUAL_ENTREPRENEUR = '2'

    LEVEL = (
        (FACTORY, 'Завод'),
        (RETAIL_NETWORK, 'Розничная сеть'),
        (INDIVIDUAL_ENTREPRENEUR, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=100, verbose_name='название поставщика')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='контакт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    level = models.CharField(max_length=50, choices=LEVEL, verbose_name='уровень')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'


class Seller(models.Model):
    """ Модель продавца """

    name = models.CharField(max_length=100, verbose_name='название продавца')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='контакт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продавец'
        verbose_name_plural = 'продавцы'
