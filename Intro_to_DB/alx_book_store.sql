CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title varchar(130) NOT NULL,
    author_id INT FOREIGN KEY,
    price DOUBLE NOT NULL,
    publication_date DATE NOT NULL
);

CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL,
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR (215) NOT NULL,
    email VARCHAR(215),
    adddress TEXT NOT NULL,
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT FOREIGN KEY,
    order_date DATE
);

CREATE TABLE Order_Details(
    orderdetailid INT PRIMARY KEY,
    order_id INT FOREIGN KEY,
    book_id INT FOREIGN KEY
    quantity DOUBLE
)