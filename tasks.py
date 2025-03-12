import logging
import time

from celery_app import app

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(),  # Para continuar imprimindo no terminal também,
    ],
)

logger = logging.getLogger(__name__)


@app.task(queue="emails")
def send_email(email):
    logger.error("QUEUE EMAIL")
    """Simula o envio de um e-mail."""
    print(f"📨 Enviando e-mail para {email}...")
    time.sleep(2)  # Simula o tempo de envio do e-mail
    return f"E-mail enviado para {email}!"


@app.task(queue="reports")
def generate_report():
    logger.error("QUEUE REPORTS:")
    """Simula a geração de um relatório."""
    print("📊 Gerando relatório...")
    time.sleep(5)  # Simula um processo longo
    return "Relatório gerado com sucesso!"


@app.task(queue="backups")
def run_backup():
    logger.error("QUEUE BACKUPS:")
    """Simula a execução de um backup."""
    print("💾 Realizando backup do sistema...")
    time.sleep(7)  # Simula um backup longo
    return "Backup concluído!"


@app.task
def reverse(text):
    time.sleep(5)
    return text[::-1]
