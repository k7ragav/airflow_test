from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from pendulum import timezone

default_args = {
    "owner": "airflow_test_2",
    "depends_on_past": False,
    # "email": ["k7ragav@gmail.com"],
    # "email_on_failure": True,
    # "email_on_retry": True,
    "retries": 1,
    "retry_delay": timedelta(minutes=15),
    "catchup": True,
}
intervals = {
    "daily_at_8am": "0 8 */1 * *",
    "daily_at_7am": "0 7 */1 * *",
    "daily_at_6am": "0 6 */1 * *",
}
bash_command = "python /root/airflow/dags/airflow_test/{{ task.task_id }}.py "

with DAG(
        "airflow_test_dag_2",
        description="testing_airflow",
        default_args=default_args,
        schedule_interval=intervals["daily_at_6am"],
        start_date=datetime(2021, 11, 3, tzinfo=timezone("Europe/Amsterdam")),
) as airflow_test_dag:
    airflow_test_task = BashOperator(
        task_id="airflow_test_dag_2",
        bash_command=bash_command,
    )
