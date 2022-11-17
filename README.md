# In Memory Database Project

*My first foray into building out a CLI and working with data!*
<br><br>
This project utilizes python to manipulate an in memory database.
A Python class found in the `dbhelper.py` file instantiates a database and has a variety of methods to manipulate the database. Additionally, there is a `main.py` function that can be run from the command line in order to execute commands interactively.<br>
<br>
## Running the Program
In the terminal

```git clone < url >```<br>
```cd ./devoted_db```<br>
```python ./main.py```<br>

At this point, you can type any number of commands listed below. Command, Name and Value arguments are strings and the commands contain no spaces :<br>
* `BEGIN`: This will begin the transaction.
* `SET[name][value]`: Add a key, value pair to the inmemory database.
* `DELETE[name]`: Delete the key, value pair associated with the name provided. The name is the key.
* `GET[name]`: Output the value associated with the name in the DB. If the name does not exist, it will return NULL.
* `COUNT[value]`: Output the number of times the given value exists in the database.
* `RESET`: Reset the database to empty
* `ROLLBACK`: Rollback the most recent transaction (a `SET` or a `DELETE`)
* `END`: Exit the program



Some methods to allow for basic database functionality including:<br>
* `load`: loads the database from a file
* `dumpdb`: dumps json into the file after changes have been made<br>
Some methods for manipulating the data:<br>
* `set`
* `get`
* `delete`
* `counter`
* `resetdb`
* `rollback`

## Notes
### On memory:
Data is stored in a dictionary which means that the storage does not necessarily increase with each addition. Depending on the number of key value pairs in it at a given time, there is some leeway before storage increases.<br>

### On failings:
1. The `BEGIN` and `COMMIT` functionality is not implemented correctly in this version. I was unable to figure out a solution that allowed for both storage without the `BEGIN`/`COMMIT` functionality and without it. <br>
2. The "database" is not implemented within the python class, which is not ideal, because its called in every single function.<br>