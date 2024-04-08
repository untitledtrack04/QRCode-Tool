# QRCode-Tool
CLI Tool For Creating/Reading QR Codes

### Depenencies 
`pip3 install argparse opencv-python qrcode`

### Usage
qrcode-tool.py [-h] [-g GENERATE] [-r READ] [-o OUTPUT]

This tool is designed to create qr codes from the command line, and read qr codes from image files. Please note that only QR codes with black fill color and white back color
can be read properly by this tool.

options:
  -h, --help            show this help message and exit
  -g GENERATE, --generate GENERATE
                        text to be made into a qr code
  -r READ, --read READ  path to qr code file to read, data read is output to stdout
  -o OUTPUT, --output OUTPUT
                        name of file to output to pwd default is qrcode.png
