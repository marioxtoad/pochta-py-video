from config import token, password
from pochta import Delivery
from pochta.enums import AddressType, TransportType
from pochta.helpers import Order

delivery = Delivery(token, password, "token")

"""
mass: Вес РПО (в граммах).
order_num: Номер заказа. Внешний идентификатор заказа, который формируется отправителем.
fragile: Установлена ли отметка "Осторожно/Хрупкое"?
mail_category: Категория РПО.
mail_type: Вид РПО.
payment: Сумма наложенного платежа (копейки).
payment_method: Способ оплаты.
"""

order = Order(
    mass=1000,
    order_num='af134qrw124gva',
    fragile=True,
)

"""
house_to: Часть адреса: Номер здания
mail_direct: Код страны.
region_to: Область, регион
place_to: Населенный пункт
street_to: Часть адреса: Улица
address_type_to: Тип адреса.
index_to: Почтовый индекс
postoffice_code: Индекс места приема
area_to: Район
building_to: Часть здания: Строение
hotel_to: Название гостиницы
corpus_to: Часть здания: Корпус
slash_to: Часть здания: Дробь
letter_to: Часть здания: Литера
location_to: Микрорайон
office_to: Часть здания: Офис
room_to: Часть здания: Номер помещения
num_address_type_to: Номер для а/я, войсковая часть, войсковая часть ЮЯ, полевая почта
raw_address: Необработанный адрес получателя
str_index_to: Почтовый индекс (буквенно-цифровой)
vladenie_to: Часть здания: Владение
transport_type: Возможный вид транспортировки (для международных отправлений).
"""

order.set_address(
    address_type_to=AddressType.DEFAULT,
    house_to='37',
    index_to=117105,
    mail_direct=643,
    place_to='г Москва',
    postoffice_code=101000,
    region_to='г Москва',
    street_to='ш Варшавское',
    transport_type=TransportType.SURFACE,
)

"""
recipient_name: Наименование получателя одной строкой (ФИО, наименование организации)
given_name: Имя получателя
surname: Фамилия получателя
middle_name: Отчество получателя
tel_address: Телефон получателя (может быть обязательным для некоторых типов отправлений)
"""

order.set_recipient(
    given_name='Иван',
    surname='Иванов',
    middle_name='Иванович',
    tel_address=79459562067,
)

"""
height: Линейная высота (сантиметры)
length: Линейная длина (сантиметры)
width: Линейная ширина (сантиметры)
"""

order.set_dimensions(
    height=3,
    length=9,
    width=73,
)

new_shipments = delivery.orders.create_order([order])
new_batch = delivery.batches.create_batch(new_shipments['result_ids'][0])
