# Group Project 0x00 - AirBnB Clone
![AirBnB Logo](https://www.digital.ink/wp-content/uploads/airbnb_logo_detail.jpg)

## Project Description
This is the first part of the AirBnB clone Project where we will work on the backend side of the project while interfacing it with a consol application using the cmd module in python.

Data or python objects generated are stored in a json file and can be accesses using the json module in python.

##Description of the command interpreter
The interface of the application is just like the bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AitBnB website

This command line interpreter serves as the frontend of the web application where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:
* show
* create
* update
* destroy
* count

And as part of the implementation of the command line interpreter paired with the backend and file storage system, the following actions can be performed:
* Creating new objects (e.g. A new User or a new Place)
* Retrieving an object from a file, database, etc.
* Doing operations on objects (count, compute stats, etc.)
* Updating attributes of an object
* Destroying an object

## How to start it
These instructions will get you a copy of the project up and runnign on your local machine (Linux distro) for development and testing purposes

## Installion
clone the repository and run the console.py
```
$ git clone https://github.com/------/AirBnB_clone.git
```

## Usage
|   **Method**   |   **Description**   |
| -------------- | ------------------- |
| [create](./console.py) | Creates object of given class |
| [show](./console.py) | Prints the string representation of an instance based on the class name and id |
| [all](./console.py) | Prints all string representation of all instances based or not on the class name |
| [update](./console.py) | Updates an instance based on the class name and id by adding or updating attirbute (save the change into the JSON file) |
| [destroy](./console.py) | Deletes an instance based on the class name and id (save the change into the JSON file) |
| [count](./console.py) | Retrieve the number of instances of a class |
| [help](./console/py) | Prints information about specific command |
| [quit/EOF](./console.py) | Exit the program |

###### Example 1
```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb) create User
bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) show User bb4f4b81-7757-460b-9263-743c9ea6fef6
[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) update User bb4f4b81-7757-460b-9263-743c9ea6fef6 name Betty
['User', 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name', 'Betty']
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name': 'Betty', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) destroy User bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb)
```
