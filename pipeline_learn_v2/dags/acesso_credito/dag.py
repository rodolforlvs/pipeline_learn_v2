from datetime import timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.python_operator import PythonOperator
# from airflow.operators import PythonOperator
from airflow.utils.dates import days_ago

from acesso_credito.tasks.task_get_file import get_files
from acesso_credito.tasks.task_bronze import move_bronze
from acesso_credito.tasks.task_silver import move_silver
from acesso_credito.tasks.task_gold import move_gold

# [END import_module]

# [START default_args]
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
# [END default_args]

# [START instantiate_dag]
with DAG(
    'acesso_credito',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['credito'],
) as dag:
    # [END instantiate_dag]

    task_get_file = PythonOperator(
        task_id='task_get_file',
        provide_context=True,
        python_callable=get_files,
        dag=dag
    )

    task_bronze = PythonOperator(
        task_id='task_bronze',
        provide_context=True,
        python_callable=move_bronze,
        dag=dag
    )

    task_silver = PythonOperator(
        task_id='task_silver',
        provide_context=True,
        python_callable=move_silver,
        dag=dag
    )

    task_gold = PythonOperator(
        task_id='task_gold',
        provide_context=True,
        python_callable=move_gold,
        dag=dag
    )

    task_get_file >> task_bronze >> task_silver >> task_gold
# # [END tutorial]