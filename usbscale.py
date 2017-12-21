#!/usr/bin/python3
import os
import fcntl
import struct
import time


# inspired by http://kubes.org/src/usbscale.c

def open_hid(dev="/dev/usb/hiddev0"):
    fd = os.open(dev, os.O_RDONLY)

    def _IOC(iodir, iotype, ionr, iosize):
        return (iodir << 30) | (iotype << 8) | (ionr << 0) | (iosize << 16)

    def HIDIOCGNAME(len):
        return _IOC(2, ord("H"), 6, len)

    name = fcntl.ioctl(fd, HIDIOCGNAME(100), " "*100).split("\0",1)[0]
    hiddev_event_fmt = "Ii"
    ev = []
	
    for _ in range(8):
        ev.append(struct.unpack(hiddev_event_fmt, os.read(fd, struct.calcsize(hiddev_event_fmt))))
    
    input_large = ev[6][1]
    input_small = ev[7][1]
    
    return name, input_small % 256, input_large % 256

def tare(inputs):
    return max(inputs)

min_threshold  = 0.8


def getWeight():    
    scale_factor = 1.0

    #print open_hid()
    smalls = [ ]
    larges = [ ]
    for _ in range(5):
        name, small, large = open_hid()
        smalls.append(small)
        larges.append(large)
    base_small = max(smalls)
    #print(smalls, larges)
    print(smalls, "->", base_small)
    base_large = max(larges)
    
    print(larges, "->", base_large)
    print("Tared...")
    time.sleep(1.5)
    
    measurements = []
    
    for _ in range(15):
        name, small, large = open_hid()
        if large < base_large + 1:
            large = 0
        else:
            large = float((large - (base_large + 1)) * 94 + ((256 - base_small) / scale_factor))
        if large == 0:
            if small >= base_small:
                small = float((small - base_small) / scale_factor)
            else:
                small = 0
        else:
            small = float((small - base_small) / scale_factor)
        if(large+small != 0):
            measurements.append(large+small)
        time.sleep(0.1)

    initial = sum(measurements)/len(measurements)
    new_w = initial
    while(new_w > min_threshold * initial):
        print(new_w)
        name, small, large = open_hid()
        if large < base_large + 1: large = 0
        else: large = (large - (base_large + 1)) * 94 + (256 - base_small) / scale_factor
        if large == 0:
            if small >= base_small : small = (small - base_small) / scale_factor
            else: small = 0
        else:
            small = (small - base_small) / scale_factor
        new_w = large + small
        time.sleep(1)
    print("Call graybar. Now!","Only " + str(new_w/initial * 100) + "% left")
    
if __name__ == "__main__":
    getWeight()
