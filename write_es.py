from connect import *
import uuid

document_1 = {
    "first_name": "supriya",
    "last_name": "sontakke",
    "address": "london",
    "transaction_date": "2021-12-10T13:12:00",
    "color":"fair",
    "age":29
}

def write_es_query(document_1, es_index="app_wallet_01"):
    my_instance.index(index=es_index, body=document_1, id=str(uuid.uuid4()))

write_es_query(document_1)
