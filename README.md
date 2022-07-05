# Usage

###### created by Weber Huang

```bash
$ git clone https://github.com/Weber12321/celery_template.git 

$ cd celery_template
```

```bash
$ vim .env

REDIS=redis://<ip>:6379/0
```

```bash
$ docker build -t ychuang/celery_client --no-cache .

$ docker run -it -d --name celery_client --env-file .env ychuang/celery_client

$ docker exec -it celery_client bash

$ python

>>> from app import sample_task
>>> from celery.result import AsyncResult
>>> sample_task.apply_async(args=(1234, ), queue='A_queue')
>>> task_id = sample_task.id
>>> result = AsyncResult(task_id)
>>> result.get()
```

