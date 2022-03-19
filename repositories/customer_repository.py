from db.run_sql import run_sql

def save(customer):
    sql = "INSERT INTO customers (first_name, last_name, email, notes) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [customer.first_name, customer.last_name, customer.email, customer.notes]
    results = run_sql(sql, values)
    customer.id = results[0]['id']
    return customer 

def delete_all():
    sql = "DELETE FROM customers"
    run_sql(sql)
    return 