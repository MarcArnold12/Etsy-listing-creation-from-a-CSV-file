## Etsy Listing Automation Script

This script automates the creation of Etsy listings using a CSV file and Etsy's Open API v3.

### Installation

#### Prerequisites

* Python 3.x
* `requests` library

#### Install Requests Library

```bash
pip install requests
```

#### Configuration

**Etsy API Credentials:**

* Obtain your `api_key`, `api_secret`, and `access_token` from Etsy.
* Update the `API_KEY`, `API_SECRET`, and `ACCESS_TOKEN` variables in the script with your credentials.

**CSV File:**

* Prepare a CSV file with the necessary columns:
    * `title`
    * `description`
    * `price`
    * `quantity`
    * `tags`
    * `materials`
    * `shipping_profile_id`
    * `taxonomy_id`
    * `who_made`
    * `is_supply`
    * `when_made`
    * `image_paths` (comma-separated list of paths or URLs)
    * `digital_file_paths` (comma-separated list of paths)

**Example CSV format:**

```csv
title,description,price,quantity,tags,materials,shipping_profile_id,taxonomy_id,who_made,is_supply,when_made,image_paths,digital_file_paths
"Vintage Painting 1","A beautiful vintage painting.",100.00,10,"vintage,painting,art","canvas,oil","123456","789012","i_did","false","2020_2022","/path/to/image1.jpg,/path/to/image2.jpg,https://example.com/image3.jpg","/path/to/digitalfile1.pdf"
"Vintage Painting 2","Another beautiful vintage painting.",150.00,5,"vintage,painting,art","canvas,oil","123456","789012","i_did","false","2020_2022","https://example.com/image4.jpg,/path/to/image5.jpg,/path/to/image6.jpg","/path/to/digitalfile2.pdf"
```

### Usage

#### Run the Script

* Update the path to your CSV file in the script.
* Execute the script:

```bash
python create_etsy_listings.py
```

#### Script Functionality

* The script reads the CSV file.
* Creates Etsy listings.
* Uploads images.
* Uploads digital files.

### Troubleshooting

* Ensure the paths to local files are correct.
* Check your internet connection if using image URLs.
* Verify your Etsy API credentials are accurate.

### License

This project is licensed under the MIT License.
