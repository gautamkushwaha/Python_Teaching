from PIL import Image

def get_geotagging_info(file_path):
    with Image.open(file_path) as img:
        # Try to extract GPS information
        try:
            gps_info = img.info['gps']
            latitude = gps_info[2][0] + gps_info[2][1] / 60 + gps_info[2][2] / 3600
            longitude = gps_info[4][0] + gps_info[4][1] / 60 + gps_info[4][2] / 3600

            if gps_info[3] == 'S':
                latitude = -latitude

            if gps_info[1] == 'W':
                longitude = -longitude

            return latitude, longitude
        except (AttributeError, KeyError):
            # Handle the case where GPS information is not present
            return None

# Test the function
file_path = "photos/ravi.jpg"
location_info = get_geotagging_info(file_path)

if location_info:
    print("Latitude:", location_info[0])
    print("Longitude:", location_info[1])
else:
    print("No GPS information found.")
