## Etsy Listing Automation Script

This script automates the creation of Etsy listings using a CSV file and Etsy's Open API v3.

### Prerequisites

* Python 3.x
* `requests` library (install using `pip install requests`)

### Installation

There's no external installation required for this script. You just need to clone or download the repository and ensure you have Python and the `requests` library installed.

### Configuration

**1. Etsy API Credentials:**

* You'll need to obtain your API key, API secret, and access token from Etsy. You can find instructions on how to do this in the Etsy developer documentation: [https://developer.etsy.com/](https://developer.etsy.com/)
* Replace the following placeholders in the script with your actual credentials:
    * `API_KEY = 'your_api_key'`
    * `API_SECRET = 'your_api_secret'`
    * `ACCESS_TOKEN = 'your_access_token'`

**2. CSV File:**

* Prepare a CSV file with the following columns:
    * `title`
    * `description`
    * `price` (float)
    * `quantity` (integer)
    * `tags` (comma-separated list)
    * `materials` (comma-separated list)
    * `shipping_profile_id` (integer)
    * `taxonomy_id` (integer)
    * `who_made`
    * `is_supply` (boolean - "true" or "false")
    * `when_made`
    * `image_paths` (comma-separated list of paths or URLs)
    * `digital_file_paths` (comma-separated list of paths)

**Example CSV format:**

```csv
title,description,price,quantity,tags,materials,shipping_profile_id,taxonomy_id,who_made,is_supply,when_made,image_paths,digital_file_paths
"Vintage Painting 1","A beautiful vintage painting.",100.00,10,"vintage,painting,art","canvas,oil","123456","789012","i_did","false","2020_2022","/path/to/image1.jpg,/path/to/image2.jpg,https://example.com/image3.jpg","/path/to/digitalfile1.pdf"
"Vintage Painting 2","Another beautiful vintage painting.",150.00,5,"vintage,painting,art","canvas,oil","123456","789012","i_did","false","2020_2022","https://example.com/image4.jpg,/path/to/image5.jpg,/path/to/image6.jpg","/path/to/digitalfile2.pdf"
```

**3. Script Location:**

* Save the script as `create_etsy_listings.py` in your project directory.

### Usage

1. Update the path to your CSV file in the script (replace `"path/to/your/listings.csv"` with your actual path).
2. Run the script from your terminal:

```bash
python create_etsy_listings.py
```

### Script Functionality

* The script reads the CSV file.
* Creates Etsy listings for each row of data.
* Uploads images (supporting both local paths and URLs).
* Uploads digital files (if present in the CSV).

### Troubleshooting

* Ensure your Etsy API credentials are correct.
* Verify the paths to local files in your CSV are accurate.
* Check your internet connection for image downloads and listing creation.
* The script includes a one-second delay between uploads to avoid hitting Etsy's rate limits. Adjust this delay if necessary.

### License

This project is licensed under the MIT License.
