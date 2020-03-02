CREATE TABLE IF NOT EXISTS public.categories
(
    category_id Serial Primary Key,
    categoryname character varying(50) COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default"
);


CREATE TABLE IF NOT EXISTS public.customers
(
    customer_id Serial Primary Key,
    customername character varying(150) COLLATE pg_catalog."default",
    contactname character varying(150) COLLATE pg_catalog."default",
    address character varying(250) COLLATE pg_catalog."default",
    city character varying(150) COLLATE pg_catalog."default",
    postalcode integer,
    country character varying(150) COLLATE pg_catalog."default"
);


CREATE TABLE IF NOT EXISTS public.employees
(
    employee_id Serial Primary Key,
    lastname character varying(155) COLLATE pg_catalog."default",
    firstname character varying(155) COLLATE pg_catalog."default",
    birthdate date,
    photo bytea,
    notes text COLLATE pg_catalog."default"
);


CREATE TABLE IF NOT EXISTS public.orderdetails
(
    order_id Serial Primary Key,
    productid integer,
    quantity integer
);

CREATE TABLE IF NOT EXISTS public.orders
(
    customer_id Serial Primary Key,
    employeeid integer,
    orderdate date,
    shipperid integer
);


CREATE TABLE IF NOT EXISTS public.products
(
    product_id Serial Primary Key,
    productname character varying(255) COLLATE pg_catalog."default",
    supplierid integer,
    categoryid integer,
    unit text COLLATE pg_catalog."default",
    price double precision
);


CREATE TABLE IF NOT EXISTS public.shippers
(
    shippername character varying(50) COLLATE pg_catalog."default",
    phone character varying(50) COLLATE pg_catalog."default"
);


CREATE TABLE IF NOT EXISTS public.suppliers
(
    supplier_id Serial Primary Key,
    suppliername character varying(50) COLLATE pg_catalog."default",
    contactname character varying(50) COLLATE pg_catalog."default",
    address character varying(50) COLLATE pg_catalog."default",
    city character varying(50) COLLATE pg_catalog."default",
    postalcode character varying(50) COLLATE pg_catalog."default",
    country character varying(50) COLLATE pg_catalog."default",
    phone character varying(50) COLLATE pg_catalog."default"
);