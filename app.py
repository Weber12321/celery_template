from celery import Celery


app = Celery(
    name='proj_B',
    broker="redis://localhost:6379"
)

app.conf.task_routes = {
    'app.training': {'queue': 'training'},
    'app.predict': {'queue': 'predict'},
}


@app.task(bind=True, queue='training', name='training')
def training(
        model_name,
        version,
        dataset,
        label_col,
        learning_rate,
        epochs,
        batch_size,
        max_len,
        is_multi_label
):
    pass


@app.task(bind=True, queue='predict', name='predict')
def predict(
        model_name,
        version,
        max_len,
        dataset
):
    pass
