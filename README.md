# PetsAndOwners

Python: 3.11

Django: 4.2

Docker: 27.3.1

Docker Compose: 2.17.3

## SetUp:

```
docker-compose build backend # build
docker-compose up            # start
docker-compose down          # stop
```

## Django Admin user:

```
Username: db-admin
Password: pass
```

## Endpoints

## Owners:

**List of owners:**
* http://localhost:8000/pao/owners/


**Owner by id:**
* http://localhost:8000/pao/owner/\<int:id\>

Get - Get owners name

Put - Change owners name

Post data example:
```
{
    "name": "Alice"
}
```

Delete - Delete owner

**Create new owner:**

* http://localhost:8000/pao/owner/

Post data example:
```
{
    "name": "Bob"
}
```

**List owners pets**
* http://localhost:8000/pao/owner/\<int:id\>/pets

## Pets:

**List of pets:**
* http://localhost:8000/pao/pets/


**Pet by id:**
* http://localhost:8000/pao/pet/\<int:id\>

Get - Get pets info

Put - Change pets info

Post data example:
```
{
    "name": "Whiskers",
    "pet_type": "cat"
}
```

Delete - Delete pet

**Create new pet:**

* http://localhost:8000/pao/pet/

Post data example:
```
{
    "name": "Fido",
    "pet_type": "dog"
}
```
## Shop:

* http://localhost:8000/pao/shop/
Post data example for owner(id=1) selling pet(id=1):
```
{
    "owner_id": 1,
    "pet_id": 1,
    "action": "sell"
}
```
Post data example for owner(id=1) buying pet(id=1):
```
{
    "owner_id": 1,
    "pet_id": 1,
    "action": "buy"
}
```

## Stats:

* http://localhost:8000/pao/stats/shared-owners-count

How many owners have the same pets (count)




