def write_notification(email: str, message=""):
    with open("/tmp/log.txt", mode='w') as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)