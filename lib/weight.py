#!/usr/bin/python3
#This code was for a prototype that we built prior to the final prototype. This is not used
import os
import struct
import time


# inspired by http://kubes.org/src/usbscale.c

def open_hid(dev="/dev/usb/hiddev0"):
    fd = os.open(dev, os.O_RDONLY)

    def _IOC(iodir, iotype, ionr, iosize):
        return (iodir << 30) | (iotype << 8) | (ionr << 0) | (iosize << 16)

    def HIDIOCGNAME(len):
        return _IOC(2, ord("H"), 6, len)

    #name = fcntl.ioctl(fd, HIDIOCGNAME(100), " "*100).split("\0",1)[0]
    hiddev_event_fmt = "ii"
    ev = []
    
    for _ in range(8):
        ev.append(struct.unpack(hiddev_event_fmt, os.read(fd, struct.calcsize(hiddev_event_fmt))))
    
    input_large = ev[6][1]
    input_small = ev[7][1]
    
    return input_small, input_large % 256

def tare(inputs):
    return max(inputs)

min_threshold  = 0.8

def getnewweight(small, large, base_small, base_large):
    if large < base_large + 1: large = 0
    else: large = (large - (base_large + 1)) * 94 + (256 - base_small)
    if large == 0:
        if small >= base_small : small = (small - base_small)
        else: small = 0
    else:
        small = (small - base_small)
    return large + small


def getWeight(product):    
    #scale_factor = 1.0

    #print open_hid()
    smalls = [ ]
    larges = [ ]
    for _ in range(5):
        start = time.time()
        small, large = open_hid()
        print("open_hid took: ",time.time() - start)
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
    start = time.time()
    for _ in range(15):
        small, large = open_hid()
        newmeasurement = getnewweight(small, large, base_small, base_large)
        if(newmeasurement != 0):
            measurements.append(newmeasurement)
        print("So far this loop took: ", time.time() - start)
        #time.sleep(0.1)

    initial = sum(measurements)/len(measurements)
    new_w = initial
    while(new_w > min_threshold * initial):
        print(new_w)
        small, large = open_hid()
        new_w = getnewweight(small, large, base_small, base_large)
        
        time.sleep(1)
    print(new_w)
    return "Call graybar. Now!" + "Only " + str(new_w/initial * 100) + "% of" + product + "left"

if __name__ == "__main__":
    getWeight()
