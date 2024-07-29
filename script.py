import csv
import requests
import json
import time
import os

# Etsy API credentials
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'

# Endpoints
CREATE_LISTING_URL = "https://openapi.etsy.com/v3/application/shops/YOUR_SHOP_ID/listings"
UPLOAD_IMAGE_URL_TEMPLATE = "https://openapi.etsy.com/v3/application/listings/{}/images"
UPLOAD_FILE_URL_TEMPLATE = "https://openapi.etsy.com/v3/application/listings/{}/files"

# Function to create a listing
def create_listing(data):
    headers = {
        "x-api-key": API_KEY,
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(CREATE_LISTING_URL, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        listing_id = response.json().get("listing_id")
        print(f"Listing created successfully with ID: {listing_id}")
        return listing_id
    else:
        print(f"Failed to create listing: {response.status_code} - {response.text}")
        return None

# Function to upload an image from a local path
def upload_image_from_path(listing_id, image_path):
    url = UPLOAD_IMAGE_URL_TEMPLATE.format(listing_id)
    headers = {
        "x-api-key": API_KEY,
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    files = {"image": open(image_path, "rb")}
    
    response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 201:
        print("Image uploaded successfully!")
    else:
        print(f"Failed to upload image: {response.status_code} - {response.text}")

# Function to upload an image from a URL
def upload_image_from_url(listing_id, image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        url = UPLOAD_IMAGE_URL_TEMPLATE.format(listing_id)
        headers = {
            "x-api-key": API_KEY,
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
        files = {"image": ('image.jpg', response.content)}
        
        upload_response = requests.post(url, headers=headers, files=files)
        
        if upload_response.status_code == 201:
            print("Image uploaded successfully from URL!")
        else:
            print(f"Failed to upload image from URL: {upload_response.status_code} - {upload_response.text}")
    else:
        print(f"Failed to download image from URL: {response.status_code} - {response.text}")

# Function to upload a digital file
def upload_digital_file(listing_id, file_path):
    url = UPLOAD_FILE_URL_TEMPLATE.format(listing_id)
    headers = {
        "x-api-key": API_KEY,
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    files = {"file": open(file_path, "rb")}
    
    response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 201:
        print("Digital file uploaded successfully!")
    else:
        print(f"Failed to upload digital file: {response.status_code} - {response.text}")

# Function to read CSV and create listings
def create_listings_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            listing_data = {
                "title": row["title"],
                "description": row["description"],
                "price": row["price"],
                "quantity": row["quantity"],
                "tags": row["tags"].split(","),
                "materials": row["materials"].split(","),
                "shipping_profile_id": row["shipping_profile_id"],
                "taxonomy_id": row["taxonomy_id"],
                "who_made": row["who_made"],
                "is_supply": row["is_supply"],
                "when_made": row["when_made"]
            }
            
            listing_id = create_listing(listing_data)
            
            if listing_id:
                # Upload images
                image_paths = row["image_paths"].split(",")
                for image_path in image_paths:
                    if image_path.startswith("http://") or image_path.startswith("https://"):
                        upload_image_from_url(listing_id, image_path)
                    else:
                        upload_image_from_path(listing_id, image_path)
                    time.sleep(1)  # Avoid rate limit
                
                # Upload digital files
                if row.get("digital_file_paths"):
                    digital_file_paths = row["digital_file_paths"].split(",")
                    for file_path in digital_file_paths:
                        upload_digital_file(listing_id, file_path)
                        time.sleep(1)  # Avoid rate limit

# Path to your CSV file
csv_file_path = "path/to/your/listings.csv"

# Create listings
create_listings_from_csv(csv_file_path)
