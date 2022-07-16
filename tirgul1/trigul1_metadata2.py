import os

import pytest
import tifffile
JPEG_SOI = b"\xFF\xD8"


def decode_metadata(file_path, meta):
    # opening in binary the path fie and closing him (after the tab)
    with open(file_path, "rb") as input_img:
        data = input_img.read()
        exif_location = find_exif_location(data)

        # extract the 'tiff' part and write it to the temp file
        output_path = "tmp.tiff"
        if os.path.exists(output_path):
            os.remove(output_path)
        tiff_file = open(output_path, "wb")
        tiff_file.write(data[exif_location+6:])
        tiff_file.close()
        with tifffile.TiffFile(output_path) as tif:
            tif_tags = {}
            for page in tif.pages:
                for tag in page.tags.values():
                    name, value = tag.name, tag.value
                    tif_tags[name.lower()] = value

    # print(tif_tags)
    if meta.lower() in tif_tags.keys():
        return tif_tags[meta.lower()]
    else:
        return -1


def find_exif_location(data):
    if data[:2] != JPEG_SOI:
        raise Exception("INVALID FILE FORMAT")
    # finding where Exif begins
    location = data.find(b"\xFF\xE1")
    # checking if the file contains Exif
    if location == -1:
        raise Exception("ERROR EXIF MARKER NOT FOUND")
    exif_location = location + 4
    # checking if the location of Exif is correct
    if data[exif_location:exif_location + 4] != b"Exif":
        raise Exception("ERROR EXIF NOT FOUND")
    return exif_location


def test_file_format():
    # assert decode_metadata('img_input\\man.bmp', '') == "INVALID FILE FORMAT"
    try:
        decode_metadata('img_output\\man.bmp', '')
        assert False
    except Exception as e:
        assert str(e) == "INVALID FILE FORMAT"


def test_file_format2():
    # assert decode_metadata('img_input\\house.bmp', '') == "Invalid file type, expected jpeg"
    try:
        decode_metadata('img_output\\house.bmp', '')
        assert False
    except Exception as e:
        assert str(e) == "INVALID FILE FORMAT"


def test_jpeg1():
    value = decode_metadata('img_input\\art.jpg', 'artist')
    assert value == 'IPTC CONTACT PANEL: CREATOR'


def test_jpeg1_wrong_meta():
    value = decode_metadata('img_input\\art.jpg', 'subject')
    assert value == -1


def test_jpeg2():
    value = decode_metadata('img_output\\new_dog.jpg', 'imagedescription')
    assert value == 'dog'


def test_jpeg2_2():
    value = decode_metadata('img_output\\new_dog.jpg', 'copyright')
    assert value == 'ido3'


def test_jpeg2_wrong_meta():
    value = decode_metadata('img_output\\new_dog.jpg', 'badmeta')
    assert value == -1