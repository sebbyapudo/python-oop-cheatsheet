# Object oriented programming in Python
# Static and class attributes

class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def upgrade_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        print('Converting to string')
        return self.name + ": " + self.membership_type

    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False


customers = [Customer('Sebby', 'Gold'),
             Customer('Angela', 'Silver')]

print(customers[0] == customers[1])

