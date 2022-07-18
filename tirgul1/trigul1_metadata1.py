def print_meta(file, meta):
    if meta in tags_dict:
        raise Exception("INFO: Tag is supported")
        with open(file, 'rb') as image_file:

def build_tags_dict():
    tags_dict[""] = 0x010e
    tags_dict["make"]=0x010f
    tags_dict["model"]=0x0110



tags_dict = dict()
build_tags_dict()
print_meta('img_input\\art.jpg', "Title")
