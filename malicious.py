#!/usr/bin/env python2
import os.path as path
import pymodbus
import struct
import binascii
# Modbus TCP parameters
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.client.sync import ModbusTcpClient
import struct

PLC_HOST = '192.168.1.149'  # need to change on another wi-fi
PLC_PORT = 502

# Modbus Address of the data to be modified (Coil or Holding Register)
MODBUS_ADDRESS = 00001  # 00001-09999
ADDITIONAL_TEXT_ADDRESS = 40001  # 40001-49999
WRITE_HOLDING_FUNCTION_C = 16
WRITE_COLI_FUNCTION_C = 15

# Additional text to be added
ADDITIONAL_TEXT = "otorio rocks " * 10  # cant do 50 in one time because it is more than 2 bytes
IMAGE_PATH = '/home/matand/projects/modbus/tcpproxy/cat.jpg' # change to path of the pic, should be in pictures

def fragment_image(image_path):
    fragments = []
    with open(image_path, "rb") as image_file:
        while True:
            fragment = image_file.read(251)  # less than 1 bytes of length at the time for length field to be correct
            if not fragment:
                break
            fragments.append(fragment)
    return fragments

def packing(t,l,c):
    transaction = t
    identifier = 0x0000
    length = l
    unitid = 0x01
    fcode = 0x01
    reg_addr = 0x000  # Register address.
    count = c

    total_pack_string = '0x{:04x}{:04x}{:04x}{:02x}{:02x}{:04x}{:04x}'.format(
        transaction, identifier, length, unitid, fcode, reg_addr, count
    )
    total_pack_hex = hex(int(total_pack_string, 16))

    pack_ = struct.pack(
        '>HHHBBHH', transaction, identifier, length, unitid, fcode, reg_addr, count
    )

    # Then send the pack_ or total_pack_hex using a TCP-Socket
    return pack_

def write_to_reg():
    # Connect to the Modbus TCP server (PLC)
    client = ModbusTcpClient(PLC_HOST, port=PLC_PORT)
    try:
        # Convert the additional text to bytes
        additional_text_bytes = ADDITIONAL_TEXT.encode('utf-8')

        # Read the original data from the Modbus address (Holding Registers)
        response = client.read_holding_registers(address=MODBUS_ADDRESS, count=len(additional_text_bytes))

        if response.isError():
            print("Error reading data from Modbus:", response)
            return

        original_data = response.registers

        # Create the modified data to be written
        data_to_write = create_encapsulated_packet(original_data)

        # Write the combined data back to the Modbus address (Holding Registers)
        response = client.write_registers(address=ADDITIONAL_TEXT_ADDRESS, values=data_to_write)

        if response.isError():
            print("Error writing data to Modbus:", response)
        else:
            print("Data written successfully:", ADDITIONAL_TEXT)

    finally:
        # Close the Modbus TCP connection
        client.close()


def create_encapsulated_packet(original_data):
    # Function to create an encapsulated packet with additional text

    # Convert the additional text to bytes
    additional_text_bytes = ADDITIONAL_TEXT.encode('utf-8')

    # Calculate the total length of the payload (original data + additional text)
    total_payload_length = len(original_data) + len(additional_text_bytes)

    data_to_write = list(original_data)
    # Add the original data to the payload
    text_list = [ord(char) for char in ADDITIONAL_TEXT]
    data_to_write.extend(text_list)

    # Return the encapsulated payload as a list of integers
    return data_to_write


class Module:
    def __init__(self, incoming=False, verbose=False, options=None):
        self.name = path.splitext(path.basename(__file__))[0]
        self.description = 'Simply print the received data as text'
        self.incoming = incoming  # incoming means module is on -im chain
        self.counter = 0
        self.image_frag = fragment_image(IMAGE_PATH)

    def execute(self, data):
        # assignment 1 "otorio rocks"
        # byte_count = chr(len(ADDITIONAL_TEXT) + 1)  # byte per char + 1 byte for previous data
        # length = chr(len(ADDITIONAL_TEXT) + 4) # 3 more bytes for unit address ,func code and byte count fields
        # new_data = data[:-5] + length + data[-4:-2] + byte_count + data[
        #     -1] + ADDITIONAL_TEXT  # makes change in the byte count and length fields
        # # print(data.encode('hex'))
        # # print (new_data.encode('hex'))
        # return new_data
        # assignment 2 cat image
        # implementation of the fragmentation the same as added assignment 1
        if self.counter < len(self.image_frag):
            byte_count = chr(len(self.image_frag[self.counter -1])+1)
            length = chr(len(self.image_frag[self.counter -1])+4)
            self.counter += 1
            new_data = data[:-5] + length + data[-4:-2] + byte_count + data[-1] + self.image_frag[self.counter]
            print(data.encode('hex'))
            print (new_data.encode('hex'))
            return new_data
        else:
            return data

    def help(self):
        return ""


if __name__ == '__main__':
    print 'This module is not supposed to be executed alone!'
