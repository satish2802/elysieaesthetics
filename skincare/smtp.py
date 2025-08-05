import smtplib

try:
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10)
    server.set_debuglevel(1)  # Enable debug output
    server.login("satishchaurasia17e@gmail.com", "mrbg evxr mmxo prsd")
    print("✅ Gmail login success!")
    server.quit()
except Exception as e:
    print("❌ Failed:", e)