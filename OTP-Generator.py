import random

def generate_otp(length):
    otp = ""
    for _ in range(length):
        otp += str(random.randint(0, 9))
    return otp

otp_length = 6  # Length of the OTP
otp = generate_otp(otp_length)
print("Generated OTP:", otp)
