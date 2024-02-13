from conexao import Conexao

while True:

    print('\n')
    mensagem = input('Mensagem: ')

    queues = Conexao().get_all_queues()
    conn = Conexao().get_conection()
    channel = conn.channel()

    for fila in queues:
        channel.queue_declare(queue=fila)
        channel.basic_publish(exchange='', routing_key=fila, body=mensagem)
        print("Mensagem enviada: %r" % mensagem + ' na fila ' + fila)
        
    conn.close()