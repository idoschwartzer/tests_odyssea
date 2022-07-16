# gets jpeg file path return tiff file path
import tifffile
JPEG_SOI = b"\xFF\xD8"
def jpeg_to_tiff(jpeg_path, meta):
    with open(jpeg_path, "rb") as input_img: # opening in binary the path fie and closing him (after the tab)
        data = input_img.read()
        if data[:2] != JPEG_SOI:  # checking if the file starts with jpeg marker
            print("INVALID FILE FORMAT")
            return -1
        location = data.find(b"\xFF\xE1") # finding where Exif begins
   
        if location == -1: #checking if the file contains Exif
            print("ERROR EXIF MARKER NOT FOUND")
            return -1
        exif_location = location + 4
        if data[exif_location:exif_location+4] != b"Exif": # checking if the location of Exif is correct
            print("ERROR EXIF NOT FOUND")
            return -1
        output_path = "tmp.tiff"    # assuming there isn't such file in curr dir
        tiff_file = open(output_path, "wb")
        tiff_file.write(data[exif_location+6:])
        tiff_file.close()
        with tifffile.TiffFile(output_path) as tif:
            tif_tags = {}
            for tag in tif.pages[0].tags.values():
                name, value = tag.name, tag.value
                tif_tags[name] = value

        # deleting the tiff file

    print(tif_tags)
    if meta in tif_tags.keys():
        return tif_tags[meta]
    else:
        return -1


print(jpeg_to_tiff("img_input/art.jpg","aaaaaaa"))
print(jpeg_to_tiff("img_input/dog.jpg","aaaaaaa"))