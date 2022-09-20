import sys
import os
import argparse
import time
import ast
from PIL import ImageGrab
import pyautogui

def capture(dur:int, area=[(0,0), (0,0)], path=''):
    if area[0]==(0,0) or area[1]==(0, 0):
        x, y= pyautogui.size()
        coords_x=(0, x)
        coords_y=(0, y)
    else:
        coords_x = (area[0][0], area[0][1])
        coords_y = (area[1][0], area[1][1])
    starttime = time.time()
    endtime = starttime+dur
    nimg=1
    
    print('Capturing area:', (coords_x[0], coords_y[0], coords_x[1], coords_y[1]), 'for %i seconds' % dur) 
    print('Files will be saved at %s' % (path.replace('none', os.path.abspath(os.path.dirname(__file__))+'/') if path=='none' else path))
    print("Working...")
    
    while time.time()<endtime:        
        img = ImageGrab.grab(bbox=(coords_x[0], coords_y[0], coords_x[1], coords_y[1]))
        try:
            img.save('%s%i.png' % (path.replace('none', '') if path=='none' else path, nimg))
        except FileNotFoundError:
            print("An error occured while saving the img file. Check if the folder exists or the path informed is correct.")
            sys.exit(1)
        except PermissionError:
            print("An error occured while saving the file. Check folder path permissions.")
            sys.exit(1)
        finally:
            img.close()
        nimg+=1

def coord_type(string):
    try:
        return (ast.literal_eval(string)[0], ast.literal_eval(string)[1])
    except:
        print ("An error occurred configuring area parameters. Check its format: \"(int, int)\". Ex.:\"(0, 800)\"")
        sys.exit(1)

def execute():
    parser = argparse.ArgumentParser(prog="Screen capture", description="Captures screenshots as .png images during a defined period of time.")
    
    parser.add_argument("-d","--duration",
                    default=15,                    
                    help="The duration in seconds. Default is 15",
                    type=int
                    )
    parser.add_argument("-ar","--area",
                    default=[(0,0), (0, 0)],                                     
                    help="The horizontal and vertical area coordinates to capture. \n" \
                    "For ex.: screencap -ar \"(320, 2240)\" \"(0, 1080)\" captures center 1920 x 1080 in a widescreen.\n" \
                    "The default is the full screen.",
                    type=coord_type,
                    nargs=2
                    )
    
    parser.add_argument("-p","--path",
                    default="none",                     
                    help="The full path folder where the .png files will be saved."\
                        "For ex.:/usr/temp/ \n\n"\
                        "Note that if a path is informed without bar at the end, the last word will be a file prefix.\n"\
                        "For ex.: /usr/temp files will be saved at /usr with names temp1.png, temp2.png and so on.",
                    type=str                    
                    )

    args = parser.parse_args()    
    
    res=capture(args.duration, args.area, args.path)

if __name__=="__main__":
    execute()