import os
from sqlalchemy import Column, Integer, String, Text, Date, Numeric, \
    ForeignKey, MetaData, Table
from Serhii_Hidenko.l_11_sqlalchemy.hw.my_db import MyDb


# Initiate metadata
metadata = MetaData()

customer_table = Table(
    "customers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_name", String(64)),
    Column("contact_name", String(64)),
    Column("address", String(64)),
    Column("city", String(32)),
    Column("postal_code", String(16)),
    Column("country", String(32)),
)

category_table = Table(
    "categories",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("category_name", String(64)),
    Column("description", Text),
)

employee_table = Table(
    "employees",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("last_name", String(64)),
    Column("first_name", String(64)),
    Column("birth_date", Date),
    Column("photo", String(128)),
    Column("notes", Text),
)

order_detail_table = Table(
    "order_details",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("order_id", Integer, ForeignKey("orders.id",
                                           ondelete="CASCADE")),
    Column("product_id", Integer, ForeignKey("products.id",
                                             ondelete="CASCADE")),
    Column("quantity", Integer),
)

order_table = Table(
    "orders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("customer_id", Integer, ForeignKey("customers.id",
                                              ondelete="CASCADE")),
    Column("employee_id", Integer, ForeignKey("employees.id",
                                              ondelete="CASCADE")),
    Column("order_date", Date),
    Column("shipper_id", Integer, ForeignKey("shippers.id",
                                             ondelete="CASCADE")),
)

product_table = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("product_name", String(64)),
    Column("supplier_id", Integer, ForeignKey("suppliers.id",
                                              ondelete="CASCADE")),
    Column("category_id", Integer, ForeignKey("categories.id")),
    Column("unit", String(32)),
    Column("price", Numeric("10,2")),
)

shipper_table = Table(
    "shippers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("shipper_name", String(64)),
    Column("phone", String(16)),
)

supplier_table = Table(
    "suppliers",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("supplier_name", String(64)),
    Column("contact_name", String(64)),
    Column("address", String(64)),
    Column("city", String(64)),
    Column("postal_code", String(16)),
    Column("country", String(32)),
    Column("phone", String(16)),
)


if __name__ == "__main__":

    db = MyDb.create(
        username=os.environ.get("PG_USERNAME"),
        password=os.environ.get("PG_PASSWORD"),
        hostname=os.environ.get("PG_HOSTNAME"),
        database=os.environ.get("PG_DATABASE"),
        port=os.environ.get("PG_PORT")
    )

    # Create all initiated tables
    db.create_tables(metadata=metadata)
