import cv2
import argparse
import qrcode

#instanciate arg parser to handle CLI stuff and give it some strings for output.
parser = argparse.ArgumentParser(
    prog ='qrcode tool.py',
    description = 'This tool is designed to create qr codes from the command line, and read qr codes from image files. Please note that only QR codes with black fill color and white back color can be read properly by this tool.'
)
#add expected arguments with help info for -h
parser.add_argument('-g', '--generate', help='text to be made into a qr code')
parser.add_argument('-r', '--read', help='path to qr code file to read, data read is output to stdout')
parser.add_argument('-o', '--output', help='name of file to output to pwd default is qrcode.png', default='qrcode.png')

#variable to interface with provided arguments
args = parser.parse_args()

#debugging stuff.
#print(f"{args.read} is args.read.name")
#print(f"{args} is the contents of args")
#print(f"{type(args.read)} is the type of args.name")

#generate qrcode from provided text only if argument was present in command.
if args.generate != None:
    qr = qrcode.QRCode(
        box_size=5,
        border=2
    )
    qr.add_data(args.generate)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(args.output)

#this doesn't work yet I am tired and confused. later me problem
#ok, so cv2 does not work with QR Codes that are not black boxes on a white background and i wasted like 5 hours of my life to learn that.
if args.read != None:
    img = cv2.imread(args.read)
    detector = cv2.QRCodeDetector()
    data, a, b  = detector.detectAndDecode(img)
    print(f"contents of the QR Code:\n{data}")
