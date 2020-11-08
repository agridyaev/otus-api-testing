# API testing lesson

> The repository contains testing API lesson examples for "Python QA engineer" course.

## Requirements

[jsonplaceholder](https://jsonplaceholder.typicode.com/)  
[httpbin.org](https://httpbin.org/)

## Running tests

For test module `02_api_testing/test_02_formats.py` - [httpbin.org](https://httpbin.org/) API is used.  
To run these tests you have to pass `--url=https://httpbin.org/` parameter, e. g.:

```
pytest 02_api_testing/test_02_formats.py --url https://httpbin.org/
```

As alternative you can run `httpbin.org` docker container:

```
docker run -p 80:80 kennethreitz/httpbin
pytest 02_api_testing/test_02_formats.py --url http://localhost
```

For the rests of the tests - [jsonplaceholder](https://jsonplaceholder.typicode.com/) API is used.