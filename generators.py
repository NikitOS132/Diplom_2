from faker import Faker

fake = Faker()

def email_generator():
    generated_email = fake.email()
    return generated_email

def password_generator():
    generated_password = fake.password(7)
    return generated_password

def name_generator():
    generate_name = fake.first_name()
    return generate_name