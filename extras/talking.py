import africastalking

# Replace with your Africa's Talking credentials
username = "app-customer-order"  # Your Africa's Talking username
api_key = "atsk_a772794f78ca3b289e4aa2d6a36ac2d803300bd92de083bae5fb6d7493796bf5f084c18d"  # Your Africa's Talking API key

# Initialize the SDK
def initialize_at():
    try:
        africastalking.initialize(username=username, api_key=api_key)
        print("Initialization successful!")
        return True
    except Exception as e:
        print(f"Initialization failed: {e}")
        return False

# Function to send a test SMS
def send_test_sms():
    try:
        sms = africastalking.SMS
        phone_number = "+254783623070"  # Replace with a valid phone number
        message = "Testing Africa's Talking connection"

        # Attempt to send the SMS
        response = sms.send(message, [phone_number])
        print("SMS sent successfully!")
        print("Response:", response)

    except Exception as e:
        print(f"Failed to send test SMS: {e}")

# Run the connection test
if __name__ == "__main__":
    if initialize_at():  # Only attempt to send SMS if initialization succeeds
        send_test_sms()
    else:
        print("Failed to initialize Africa's Talking. Check your credentials.")
