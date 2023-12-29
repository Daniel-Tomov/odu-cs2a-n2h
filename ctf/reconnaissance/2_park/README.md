# Reconnaissance 1 - Google Reverse Image Search
Use Google Reverse Image Search to find the name of the fountain.
![](park.jpeg?raw=true)

<details>
<summary>Hint</summary>

- If you are using Chrome, right click the image and select "Search images with Google."
- If you are using a different browser, save the image and upload it to [Google Images](https://images.google.com/).

</details>

<details>
<summary>Answer</summary>
Franklin Square Fountain
</details>

## Alternative Method

The image has [metadata](https://csrc.nist.gov/glossary/term/metadata) embedded in it. You can view the metadata in the image using `exiftool`. Metadata is commonly known as "exif data," hence the name `exiftool`. Use `exiftool` to view the metadata of the image.

```bash
exiftool park.jpg
```
A long list of embedded data is returned. Everything from when the image was taken to the GPS coordinates of where the image was taken. Metadata in images is commonly used as an easy or medium level challenge in CTFs. Questions may be one of the following:

- What is the model of the phone which took this picture? Or what year was the phone manufactured?
- What is the make of the camera that took the picture?
- What is the location of where the image was taken? What city was the image taken in?

Back to the image above, we need to look at the GPS metadata. There is a longitude and latitude towards the bottom of the output of exiftool. 

```
GPS Position                    : 39 deg 57' 19.83" N, 75 deg 9' 1.68" W
```

You can put these coordinates in a website to get an address. I use [gps-coordinates.net](https://www.gps-coordinates.net/)


<details>
<summary>Answer</summary>

![](park_gps.jpg?raw=true)

</details>