import time

from kombu import Queue

from celery_app import app


@app.task(queue="emails")
def send_email(email):
    print("QUEUE EMAIL", Queue("emails"))
    """Simula o envio de um e-mail."""
    print(f"📨 Enviando e-mail para {email}...")
    time.sleep(2)  # Simula o tempo de envio do e-mail
    return f"E-mail enviado para {email}!"


@app.task(queue="reports")
def generate_report():
    print("QUEUE reports", Queue("reports"))
    """Simula a geração de um relatório."""
    print("📊 Gerando relatório...")
    time.sleep(5)  # Simula um processo longo
    return "Relatório gerado com sucesso!"


@app.task(queue="backups")
def run_backup():
    print("QUEUE backup", Queue("backups"))
    """Simula a execução de um backup."""
    print("💾 Realizando backup do sistema...")
    time.sleep(7)  # Simula um backup longo
    return "Backup concluído!"


@app.task
def reverse(text):
    time.sleep(5)
    return text[::-1]
