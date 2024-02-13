import pika
from pyrabbit.api import Client

class Conexao:

    def __init__(self) -> None:
        self.host = 'localhost'
        self.user = 'usuario'
        self.password = 'ferlkuJSEORvJIWE#432GM'
        self.api = 'localhost:15672'


    def get_conection(self) -> pika.BlockingConnection:
        return pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host,
                credentials=pika.PlainCredentials(
                    username=self.user,
                    password=self.password
                )
            )
        )
    
    def get_all_queues(self):
        cl = Client(self.api, self.user, self.password)
        queues = [q['name'] for q in cl.get_queues()]
        return queues