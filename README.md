# Usage

###### created by Weber Huang

```bash
$ git clone https://github.com/Weber12321/celery_template.git 

$ cd celery_template
```

```bash
$ vim .env

BROKER=redis://<ip>:6379
```

```bash
$ docker build -t ychuang/celery_client --no-cache .

$ docker run -it -d --name celery_client ychuang/celery_client

$ docker exec -it celery_client bash

$ python

>>> from app import sample_task
>>> sample_task.apply_async(args=(1234, ), queue=<worker_machine_queue>)
```

