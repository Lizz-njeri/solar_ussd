from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "Kwepo"
api_key = ""
africastalking.initialize(username, api_key)

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    print(phone_number)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)
    sms = africastalking.SMS

    sender="AFTKNG"

    if text == "":
        response = "CON Welcome to Sola Marketplace\n"
        response += "1. Buy Solar Panels\n"
        response += "2. Buy Solar Water Heater\n"
        response += "3. Buy Solar Battery\n"
        response += "4. Buy Inverter\n"
        response += "5. Connect with a Seller\n"

    # Solar Panels
    elif text == "1":
        response = "CON Choose Solar Panel Size:\n"
        response += "1. 100W - Small devices (lights/fans) - KES 5,000\n"
        response += "2. 300W - Small household - KES 15,000\n"
        response += "3. 500W - Medium home/business - KES 25,000\n"
        response += "4. 1000W - Large home/business - KES 40,000\n"
        response += "5. Check Stock\n"

    # Buy Solar Panel
    elif text == "1*1":
        response = "CON You selected 100W Solar Panel for KES 5,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "1*2":
        response = "CON You selected 300W Solar Panel for KES 15,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "1*3":
        response = "CON You selected 500W Solar Panel for KES 25,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "1*4":
        response = "CON You selected 1000W Solar Panel for KES 40,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "1*5":
        response = "CON Solar Panel Stock Levels:\n"
        response += "1. 100W - 50 units\n"
        response += "2. 300W - 30 units\n"
        response += "3. 500W - 20 units\n"
        response += "4. 1000W - 10 units\n"
        response += "5. Back to Menu\n"

    # Solar Water Heater
    elif text == "2":
        response = "CON Choose Solar Water Heater Capacity:\n"
        response += "1. 100 Liters - Small family - KES 20,000\n"
        response += "2. 200 Liters - Medium family - KES 35,000\n"
        response += "3. 300 Liters - Large family/business - KES 50,000\n"
        response += "4. Check Stock\n"

    elif text == "2*1":
        response = "CON You selected 100 Liters Solar Water Heater for KES 20,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "2*2":
        response = "CON You selected 200 Liters Solar Water Heater for KES 35,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "2*3":
        response = "CON You selected 300 Liters Solar Water Heater for KES 50,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "2*4":
        response = "CON Solar Water Heater Stock Levels:\n"
        response += "1. 100 Liters - 15 units\n"
        response += "2. 200 Liters - 8 units\n"
        response += "3. 300 Liters - 5 units\n"
        response += "5. Back to Menu\n"

    # Solar Battery
    elif text == "3":
        response = "CON Choose Solar Battery Capacity:\n"
        response += "1. 100Ah - Small homes - KES 10,000\n"
        response += "2. 200Ah - Medium homes - KES 20,000\n"
        response += "3. 300Ah - Off-grid homes/businesses - KES 30,000\n"
        response += "4. Check Stock\n"

    elif text == "3*1":
        response = "CON You selected 100Ah Solar Battery for KES 10,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "3*2":
        response = "CON You selected 200Ah Solar Battery for KES 20,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "3*3":
        response = "CON You selected 300Ah Solar Battery for KES 30,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "3*4":
        response = "CON Solar Battery Stock Levels:\n"
        response += "1. 100Ah - 25 units\n"
        response += "2. 200Ah - 15 units\n"
        response += "3. 300Ah - 10 units\n"
        response += "5. Back to Menu\n"

    # Inverter
    elif text == "4":
        response = "CON Choose Inverter Power Rating:\n"
        response += "1. 1.5 kVA - KES 12,000\n"
        response += "2. 3 kVA - KES 25,000\n"
        response += "3. 5 kVA - KES 40,000\n"
        response += "4. Check Stock\n"

    elif text == "4*1":
        response = "CON You selected 1.5 kVA Inverter for KES 12,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "4*2":
        response = "CON You selected 3 kVA Inverter for KES 25,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "4*3":
        response = "CON You selected 5 kVA Inverter for KES 40,000\n"
        response += "1. Order Now\n"
        response += "2. Back to Menu\n"

    elif text == "4*4":
        response = "CON Inverter Stock Levels:\n"
        response += "1. 1.5 kVA - 12 units\n"
        response += "2. 3 kVA - 8 units\n"
        response += "3. 5 kVA - 5 units\n"
        response += "5. Back to Menu\n"

    # Connect with Seller
    elif text == "5":
        response = "CON Connect with a Seller:\n"
        response += "1. Call a Seller\n"
        response += "2. Receive SMS with Seller Contacts\n"
    
    elif text == "5*1":
        response = "END Please call this number to speak to a seller: +254700000000"
    
    elif text == "5*2":
        response = "END You will receive an SMS with seller contacts shortly."
        # Optionally, send SMS using Africa's Talking SMS API
        sms.send("Seller contacts: +254700000000, +254711111111", sms_phone_number, sender)
    
    # Buy Now Confirmation
    elif text.endswith("*1"):
        response = "END Thank you for your purchase! Your order has been placed and a seller will contact you shortly."
        # You can also add a feature to send an SMS or make an API call here to confirm the purchase.
        message ="Your order has been received and is being processed."
        sms.send(message, sms_phone_number, sender)
    
    else:
        response = "END Invalid input. Please try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
