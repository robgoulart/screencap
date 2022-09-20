## What is
* CLI application that take screenshots over a period of time defined by user and save them in enumerated .png files.

* The application was created to generate GIFs showing the small games i started to develop. That's why it captures the full screen or an area defined by user.

## Installation
* Clone this repository and use in the terminal

## Usage
```console
 $ screencap -d 20 -p /usr/temp/


 $ screencap -d 30 -p /usr/temp/ -ar "(320, 2240)" "(0, 1080)"
```

## Flags
  -h, --help            Show this help message and exit
  -d, --duration        The duration in seconds. Default is 15
  -ar, --area           The horizontal and vertical area coordinates to capture.
                        Ex.: screencap -ar "(320, 2240)" "(0,1080)" captures center 1920 x 1080 in a widescreen. The default is the full screen.
  -p, --path            The full path folder where the .png files will be saved. 
                        Ex.:/usr/temp/ Note that if a path is informed without bar at the end, the last word will be a file prefix. 
                        Ex.: /usr/temp files will be saved at /usr with names temp1.png, temp2.png and so on.
