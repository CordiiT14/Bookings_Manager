class Customer:

    def __init__(self, first_name, last_name, email, notes = None, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.notes = notes
        self.id = id

    def full_name(self, customer):
        full_name = f"{customer.first_name} {customer.last_name}"
        return full_name