import logging
import time

from celery.result import AsyncResult

from tasks import generate_report, run_backup, send_email

logger = logging.getLogger(__name__)


EMAIL_DEMAND_IDS = [1, 2, 3, 4, 5]
REPORT_DEMAND_IDS = [6, 7, 8, 9, 10]
BACKUP_DEMAND_IDS = [11, 12, 13, 14, 15]


if __name__ == "__main__":
    # Chamando as tarefas assíncronas
    task_email = []
    task_report = []
    task_backup = []

    for task in EMAIL_DEMAND_IDS:
        task_id = send_email.delay(f"user_{task}@email.com")
        task_email.append(task_id.id)

    for task in REPORT_DEMAND_IDS:
        task_id = generate_report.delay()
        task_report.append(task_id.id)

    for task in BACKUP_DEMAND_IDS:
        task_id = run_backup.delay()
        task_backup.append(task_id.id)

    for task_id in task_email:
        email_result: AsyncResult | None = AsyncResult(task_id)

        while email_result.status != "SUCCESS":
            print(f"Aguardando envio do e-mail na task: {task_id}...")
            time.sleep(1)
        if email_result.status == "SUCCESS":
            print(f"E-mail da task {task_id} enviado com sucesso!")
        email_result = None

    for task_id in task_report:
        report_result: AsyncResult | None = AsyncResult(task_id)

        while report_result.status != "SUCCESS":
            print(f"Aguardando envio do report na task: {task_id}...")
            time.sleep(1)
        if report_result.status == "SUCCESS":
            print(f"Report na task: {task_id} enviado com sucesso!")
        report_result = None

    for task_id in task_backup:
        backup_result: AsyncResult | None = AsyncResult(task_id)

        while backup_result.status != "SUCCESS":
            print(f"Aguardando backup na task: {task_id}...")
            time.sleep(1)
        if backup_result.status == "SUCCESS":
            print(f"Backup na task: {task_id} realizado com sucesso!")
        backup_result = None
