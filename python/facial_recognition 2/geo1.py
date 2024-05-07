"""import PIL.Image

img=PIL.Image.open("photos/ravisample.jpg")

import PIL.ExifTags

exif={
    PIL.ExifTags.TAGS[k]: v
    for k,v in img._getexif().items()
    if k in PIL.ExifTags.TAGS

}

print(exif['GPSInfo'][2])

"""
from PIL import Image, ExifTags

img = Image.open("photos/santhosh.jpg")

metadata = img.info
print("Image Metadata:", metadata)


try:
    exif_data = img._getexif()

    if exif_data is not None:
        # Create a dictionary mapping Exif tags to their values
        exif = {ExifTags.TAGS[k]: v for k, v in exif_data.items() if k in ExifTags.TAGS}

        # Check if 'GPSInfo' is present in the Exif data
        if 'GPSInfo' in exif:
            gps_info = exif['GPSInfo']

            # Extract GPS latitude information
            latitude = gps_info[2]
            print("GPS Latitude:", latitude)

        else:
            print("No GPS information found in Exif data.")

    else:
        print("No Exif data found in the image.")

except Exception as e:
    print(f"Error: {e}")
