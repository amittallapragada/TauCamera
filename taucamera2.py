import argparse
import serial
import binascii
import crc16

#Setup argparse
parser = argparse.ArgumentParser (description='Capture, transfer, and delete images from a Tau 2 640')
parser.add_argument("-c8", "--capture8", action = 'store_true', required = False, help ='captures an 8 bit image: -c8/--capture8 --port/-p [port name]')
parser.add_argument("-c14", "--capture14", action = 'store_true', required = False, help ='captures an 14 bit image: -c14/--capture14 --port/-p [port name]')
parser.add_argument('-i', '--images', action = 'store_true', required = False, help="lists out the images taken: -i/--images --port/-p [port name]")
parser.add_argument("-t", "--transfer", type=str, required = False, help="transfers a specified image from camera to ground: -t/--transfer [file name] --port/-p [port name]")
parser.add_argument("-d", "--delete" , type=str, required = False, help="deletes a specified images: -d/--delete [file name] --port/-p [port name]")
parser.add_argument("-p", "--port" , type=str, required = True, help="port name")
args = parser.parse_args()

PROCESS_CODE = 0X6e
NOOP_CODE = 0X00
ERASE_CODE = 0XD6
TRANSFER = 0X82


def createSerialObject(port):
	port_val = port
	ser = serial.Serial(port = port_val, baudrate = 57600, bytesize=serial.EIGHTBITS, timeout=1) #put in arbitrary baudrate and bytesize for testing
	return ser



def serialInputAnalyzer(inputValue):
	Proccess_Code = bytes([inputValue[0], inputValue[1]])
	return Process_Code	 		



if args.capture8:
	
	message = bytes([0x6e, 0x00, 0x00, TRANSFER, 0x00, 0x02])
	#print(message)
	crc1bytes = crc16.crc16xmodem(message).to_bytes(2, byteorder='big')
	#print(crc1bytes)
	message1 = message + crc1bytes
	#print(message1)
	message2 = message1 + bytes([0x16, 0x00])
	#crc2bytes = binascii.crc_hqx(message1, 0).to_bytes(2, byteorder='big')
	crc2bytes = crc16.crc16xmodem(message2).to_bytes(2, byteorder='big')
	#crc2bytes = crc16.crc16xmodem(bytes([0x6e, 0x01, 0x00, 0x00, 0x00, 0x00, 0xdf, 0xbb])).to_bytes(2, byteorder='big')
	#print(crc2bytes)
	message3 = message2 + crc2bytes
	print(message3)

	test_serial_obj = createSerialObject(args.port) #creates and prints a test seral object

	test_serial_obj.write(message3) #?

	readBytes = bytes(test_serial_obj.read(50))
	print(readBytes)
	print(binascii.hexlify(readBytes))


if args.capture14:

	message = bytes([0x6e, 0x00, 0x00, TRANSFER, 0x00, 0x02])
	#print(message)
	crc1bytes = crc16.crc16xmodem(message).to_bytes(2, byteorder='big')
	#print(crc1bytes)
	message1 = message + crc1bytes
	#print(message1)
	message2 = message1 + bytes([0x08, 0x00])
	#crc2bytes = binascii.crc_hqx(message1, 0).to_bytes(2, byteorder='big')
	crc2bytes = crc16.crc16xmodem(message2).to_bytes(2, byteorder='big')
	#crc2bytes = crc16.crc16xmodem(bytes([0x6e, 0x01, 0x00, 0x00, 0x00, 0x00, 0xdf, 0xbb])).to_bytes(2, byteorder='big')
	#print(crc2bytes)
	message3 = message2 + crc2bytes
	print(message3)

	test_serial_obj = createSerialObject(args.port) 

	test_serial_obj.write(message3) #?

	readBytes = bytes(test_serial_obj.read(50))
	print(readBytes)
	print(binascii.hexlify(readBytes))

if args.delete:

	#GET_NUC_ADDRESS
	NUC_ADDRESS = 0xD6
	message = bytes([0x6e, 0x00, 0x00, NUC_ADDRESS, 0x00, 0x04])
	#print(message)
	crc1bytes = crc16.crc16xmodem(message).to_bytes(2, byteorder='big')
	#print(crc1bytes)
	message1 = message + crc1bytes
	#print(message1)
	message2 = message1 + bytes([0xFF, 0xFF, 0X00, 0X13])
	#crc2bytes = binascii.crc_hqx(message1, 0).to_bytes(2, byteorder='big')
	crc2bytes = crc16.crc16xmodem(message2).to_bytes(2, byteorder='big')
	#crc2bytes = crc16.crc16xmodem(bytes([0x6e, 0x01, 0x00, 0x00, 0x00, 0x00, 0xdf, 0xbb])).to_bytes(2, byteorder='big')
	#print(crc2bytes)
	message3 = message2 + crc2bytes
	print(message3)

	test_serial_obj = createSerialObject(args.port) 

	test_serial_obj.write(message3) #?

	readBytes = bytes(test_serial_obj.read(50))
	print(readBytes)
	print(binascii.hexlify(readBytes))







	# message = bytes([0x6e, 0x00, 0x00, ERASE_CODE, 0x00, 0x02])
	# #print(message)
	# crc1bytes = crc16.crc16xmodem(message).to_bytes(2, byteorder='big')
	# #print(crc1bytes)
	# message1 = message + crc1bytes
	# #print(message1)
	# message2 = message1 + bytes([0x08, 0x00])
	# #crc2bytes = binascii.crc_hqx(message1, 0).to_bytes(2, byteorder='big')
	# crc2bytes = crc16.crc16xmodem(message2).to_bytes(2, byteorder='big')
	# #crc2bytes = crc16.crc16xmodem(bytes([0x6e, 0x01, 0x00, 0x00, 0x00, 0x00, 0xdf, 0xbb])).to_bytes(2, byteorder='big')
	# #print(crc2bytes)
	# message3 = message2 + crc2bytes
	# print(message3)

	# test_serial_obj = createSerialObject(args.port) 

	# test_serial_obj.write(message3) #?

	# readBytes = bytes(test_serial_obj.read(50))
	# print(readBytes)
	# print(binascii.hexlify(readBytes))

#if args.transfer:


#if args.delete: