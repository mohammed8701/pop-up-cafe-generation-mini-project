# Mohammed's Pop Up Cafe for Generation Mini Project
This is a Python based CLI application for a pop-up cafe. The app allows the user to create/track orders for their customers. It performed CRUD operations for their data and  stores that data in a MySQL database.


```
As a user I want to:

Create a product, courier, or order and add it to a list
View all products, couriers, or orders
Update the status of an order
Persist my data
Delete or update a product, order, or courier
```
## Getting Started

1. Clone the repo<br/>

Under the repo name click *clone or download*<br/>
Click on *use HTTPs*, copy the clone URL of the repo<br/>
In the terminal go on the working directory where you want to clone the project<br/>
Use the `git clone` command and paste the clone URL then press enter :

```shell
$ git clone https://github.com/your-username/your-repositary.git
```

2. On your local machine go inside of the *pop-up-cafe* directory :

```shell
$ cd generation-mini-project
```

### Create Docker Container for MySQL DB

1. Ensure you have Docker Desktop installed and running (you can check with `docker -v`).
2. Run the following command **inside** the directory in a terminal. This will create both the client and server for us which is running on localhost.

```
$ docker-compose up -d
```

​	You should get the following output:

```sh
Creating mysql_container   ... done
Creating adminer_container ... done
```

3. Navigate to the following URL to ensure that you can see the `Adminer` interface:

http://localhost:8080/

4. Fill in the username (`root`) and password field (`password`), leave the database field blank.

5. Select `SQL Command` on the left.
6. We'll create our own database with:

```
CREATE DATABASE popupcafe;
```
7. We'll create our tables with the following:
```
create table Products (prod_id INT NOT NULL AUTO_INCREMENT, prod_name VARCHAR(255), prod_price FLOAT, PRIMARY KEY (prod_id));
```
```
create table Couriers (c_id INT NOT NULL AUTO_INCREMENT, c_name VARCHAR(255), c_number BIGINT, PRIMARY KEY (c_id));
```
```
create table Orders (order_id INT NOT NULL AUTO_INCREMENT, order_name VARCHAR(255), order_add VARCHAR(255), order_phone INT, order_courier VARCHAR(255), order_status VARCHAR(255), order_items VARCHAR(255), PRIMARY KEY (order_id));
```





### Creating And Activating The Virtual Environment
Creating the virtual environment

On macOS and Linux:

```shell
python3 -m venv .venv
```
On Windows:
```shell
py -m venv .venv
```
Activate the virtual environment
Windows: 
```shell
$ source venv/Scripts/activate
```
MacOS/Unix: 
```shell
$ source venv/bin/activate
```


## Prerequisites

The requirements to run the project are:<br/>
cffi==1.14.4<br/>
cryptography==3.2.1<br/>
pycparser==2.20<br/>
PyMySQL==0.10.1<br/>
python-dotenv==0.15.0<br/>
six==1.15.0<br/>
cffi==1.14.4<br/>
pytest==6.2.4<br/>

To install these requirements, run in the terminal:

```shell
$ pip install -r requirements.txt
```

## Running the tests
Check that the codes are passing the test. From the tests directory, run:
```shell
$ pytest tests.py -v
```

## Author
Mohammed Ahmed
