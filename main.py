# Step 1: Import necessary libraries
import qrcode
from pico_css import create_card

# Step 2: Create QR code generation function
function generate_wifi_qr_code(ssid, password):
    wifi_data = f"WIFI:T:WPA;S:{ssid};P:{password};;"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

# Step 3: Take user input
ssid_input = input("Enter WiFi SSID: ")
password_input = input("Enter WiFi Password: ")

# Step 4: Generate QR code
wifi_qr_code = generate_wifi_qr_code(ssid_input, password_input)

# Step 5: Use Pico CSS to style QR code card
qr_code_card = create_card(content=wifi_qr_code, style="background-color: #f2f2f2; padding: 20px;")

# Display the QR code card
print(qr_code_card)
