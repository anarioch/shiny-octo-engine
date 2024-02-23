# MWNZ Evaluation

My MWNZ evaluation in python, as both a CLI app and an API in django.

The history of this repo shows the basic steps that have been taken to arrive here, and follows [Conventional Commits](https://www.conventionalcommits.org/) for readability.

## Implementation

### CLI

The CLI app [transform.py](transform.py) shows the invocation of the remote API and translation from XML to JSON.  It uses standard python idioms for a main method and argument parsing.

```
$ ./transform.py 1
{"id": "1", "name": "MWNZ", "description": "..is awesome"}
$ ./transform.py 4
Error: target API call failed with code '404'
```

### Django API

The Django app uses the same request/transform logic and exposes it behind a REST API implemented in Django.  Key notes:
* [views.py](djangoapi/transform/views.py) contains the main logic.
* I have run this locally via the Django development server `python manage.py runserver` and get the same results as via the CLI app
* [tests.py](djangoapi/transform/tests.py) contains unit tests, which both pass when invoked with `python manage.py test`

## Notes

This is a very simple implementation, matching the simplicity of the requirements.  This makes it easier to extend as further requirements are shaped.

This assumes that the target JSON data model is fixed (per requirements).  If this should be flexible and pass-through then other transform options such as `xmltodict.parse(xml_data)` could be used.

Other NFRs that could be discussed for extra robustness/scalability: authentication, caching, data model extensibility.
