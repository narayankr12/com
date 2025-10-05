def email_slicer(email):
    try:
        username, domain = email.strip().split('@')
        print(f"📧 Email: {email}")
        print(f"👤 Username: {username}")
        print(f"🌐 Domain: {domain}")
    except ValueError:
        print("❌ Invalid email format. Please include '@'.")

# Example usage
user_email = input("Enter your email address: ")
email_slicer(user_email)
