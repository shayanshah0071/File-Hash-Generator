#importing functions and libraries 
from IPython.display import display 
import ipywidgets as widgets

#using widget module to create horizontal box to upload sample file . 

upload = widgets.FileUpload(multiple=True)
label = widgets.Label(value="upload sample files over here")
hbox = widgets.HBox([label,upload])
display(hbox)
 
#creating function to create hash of value
def generate_hashes(sample: bytes ) -> dict:
    """
    Generates a dict of hashes for a given bytes sample
    """
    return{
        "md5": hashlib.md5(sample).hexdigest(),
        "sh1": hashlib.sha1(sample).hexdigest(),
        "sh256": hashlib.sha256(sample).hexdigest(),
        "sh512": hashlib.sha512(sample).hexdigest(),
    }
upload.value
#quickly make file hashes with a dict comphersion 
file_hashes: dict = { key: generate_hashes(value["content"]) for (key,value) in enumerate(upload.value)}
file_hashes
# now we will create table in HTML to render our values 
table = "<table>"
table += "<tr><th>File Name</th><th>MD5</th><th>SHA1</th><th>SHA256</th><th>SHA512</th>"
#use loop over file_hash yo add values to our table 
for f in file_hashes:
    table += f"<td>{f}</td>"
     # Use another loop for the hashes
    # Note we access the dict with the key `f`
    for h in file_hashes[f]:
        hash = file_hashes[f][h]
        table += f"<td>{hash}</td>"
    table += "</tr>"
table += "</table>"
html = widgets.HTML(value=table)
display(html)
        