[![Build Status](https://api.travis-ci.org/derymukti/pentools.svg?branch=master)](https://travis-ci.org/derymukti/pentools) [![codecov](https://codecov.io/gh/derymukti/pentools/branch/master/graph/badge.svg)](https://codecov.io/gh/derymukti/pentools)
# Pentools (Python Engine Tools) 

## How to Use
```bash
$ git clone git@github.com:derymukti/pentools.git
```
```bash
$ cd pentools
```
```bash
$ sudo pip install -r requrements.txt
```

## Config

Update config in config.json

## Basic CLI

Create new module

```bash
$ python manage.py create:module -n users
```

Initial db after create new module
```bash
$ python manage.py init_db
```
Run App
```bash
$ python manage.py run
```

## Basic api

### Create New User
[POST] http://localhost:8383/users/create_user

```json
{
	"username":"pentools",
	"password":"1234",
	"email":"test@email.com"
}
```

### Get Users
[GET] http://localhost:8383/users/get_user

### Update User
[POST] http://localhost:8383/users/update_user

```json
{
	"id":"1",
	"username":"updateuser",
	"password":"updatepassword",
	"email":"update@email.com"
}
```