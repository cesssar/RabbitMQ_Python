from conexao import Conexao

fila = input('Especifique o nome da fila: ')

conn = Conexao().get_conection()

channel = conn.channel()
channel.queue_declare(queue=fila)

def callback(ch, method, properties, body):
    print("Mensagem recebida: %r" % body)

channel.basic_consume(
    auto_ack=True,
    on_message_callback=callback,
    queue=fila
)

print(f'Aguardando mensagens na fila {fila}...')
channel.start_consuming()