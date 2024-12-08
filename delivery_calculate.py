from config import token, password
from pochta import Delivery
from pochta.enums import MailCategory, MailType

delivery = Delivery(token, password, "token")

"""
completeness_checking: Признак услуги проверки комплектности
courier: Отметка "Курьер"
declared_value: Объявленная ценность
height: Линейная высота (сантиметры)
length: Линейная длина (сантиметры)
width: Линейная ширина (сантиметры)
entries_type: Категория вложения.
fragile: Отметка "Осторожно/Хрупко"
index_from: Почтовый индекс объекта почтовой связи места приема
index_to: Почтовый индекс объекта почтовой связи места назначения
mail_category: Категория РПО
mail_direct: Код страны назначения.
mail_type: Вид РПО
mass: Масса отправления в граммах
notice_payment_method: Способ оплаты уведомеления.
payment_method: Способ оплаты.
sms_notice_recipient: Признак услуги SMS уведомления
transport_type: Вид транспортировки
with_order_of_notice: Отметка 'С заказным уведомлением'
with_simple_notice: Отметка 'С простым уведомлением'
Результат расчета доставки
"""

calc_result = delivery.nogroup.calc_delivery_rate(
    index_from='680000', # Индексы ОПС указанные в ЛК
    index_to='644015',
    mail_category=MailCategory.ORDINARY,
    mail_type=MailType.POSTAL_PARCEL,
    mass=1000,
    height=2,
    length=5,
    width=197,
    fragile=True,
)
