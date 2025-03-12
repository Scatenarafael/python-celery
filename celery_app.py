from celery import Celery
from kombu import Queue

# Configuração do Celery
app = Celery(
    "tasks",
    broker="pyamqp://user:password@localhost:5672//",  # Usando RabbitMQ como broker
    backend="db+sqlite:///results.sqlite",  # Armazenando resultados no SQLite
)

# Definição das filas
app.conf.task_queues = (
    Queue("emails"),  # Fila para envio de e-mails
    Queue("reports"),  # Fila para geração de relatórios
    Queue("backups"),  # Fila para backups
)

# Definição de roteamento automático
app.conf.task_routes = {
    "tasks.send_email": {"queue": "emails"},
    "tasks.generate_report": {"queue": "reports"},
    "tasks.run_backup": {"queue": "backups"},
}

app.conf.worker_hijack_root_logger = False
