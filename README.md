
AV_SCUA
========

AV_SCUA is a catalog of audio-visual materials held in the Iowa State
University Library's Special Collections and Archives built with Django
and the Django REST framework.

Developer set up
----------------

``` {.sourceCode .console}
> git clone https://github.com/isu-meta/av_scua.git
> cd av_scua
> python -m venv env_av_scua
> env_av_scua\
> pip install -r requirements.txt
> pip install -r requirements-dev.txt
```


With the environment created, run the Django development server.

``` {.sourceCode .console}
> python manage.py runserver
```

Changing filters
-----------------

To change the filterable fields, navigate to [dtable.html](templates/basic/dtable.html) and modify the javascript generated table data:

``` {.sourceCode .javascript}
> '<td align="right" width="150">UID:</td>'+
> '<td>'+d.uid+'</td>'+
```

Documentation
--------------

https://mddocs.readthedocs.io/en/latest/scua.html#av-database
