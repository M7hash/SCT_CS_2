# -------------------------------
# Simple Image Encryption & Decryption
# Using Pixel Manipulation + Key
# -------------------------------

from PIL import Image
import numpy as np
import os

# Encrypt Function
def encrypt_image(image_path, key):
    # Load the image
    img = Image.open(image_path)
    
    # Convert image to array
    arr = np.array(img, dtype=np.uint8)
    
    encrypted_arr = ((arr.astype(np.uint16) + key) % 256).astype(np.uint8)
    
    # Convert back to image
    encrypted_img = Image.fromarray(encrypted_arr)
    
    # Save encrypted image
    output = os.path.splitext(image_path)[0] + "_encrypted.png"
    encrypted_img.save(output)
    
    print("Image encrypted successfully!")
    print("Saved as:", output)


# Decrypt Function
def decrypt_image(image_path, key):
    img = Image.open(image_path)
    
    arr = np.array(img, dtype=np.uint8)
    
    decrypted_arr = ((arr.astype(np.uint16) - key) % 256).astype(np.uint8)
    
    decrypted_img = Image.fromarray(decrypted_arr)
    
    output = os.path.splitext(image_path)[0] + "_decrypted.png"
    decrypted_img.save(output)
    
    print("Image decrypted successfully!")
    print("Saved as:", output)


# MAIN PROGRAM
print("=== Image Encryption / Decryption Tool ===")
path = input("Enter image path: ")

try:
    key = int(input("Enter secret key (number): "))
except:
    print("Key must be a number!")
    exit()

print("\n1) Encrypt Image")
print("2) Decrypt Image")
choice = input("Choose option (1/2): ")

if choice == "1":
    encrypt_image(path, key)
elif choice == "2":
    decrypt_image(path, key)
else:
    print("Invalid choice!")

