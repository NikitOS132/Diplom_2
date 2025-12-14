from faker import Faker

fake = Faker()

def email_generator():
    generated_email = fake.email()
    return generated_email

def password_generator():
    generated_password = fake.password(6)
    return generated_password

def name_generator():
    generate_name = fake.first_name()
    return generate_name

def false_email_generator():
    false_email = fake.email()
    return false_email

def false_password_generator():
    password_generator = fake.password(7)
    return password_generator