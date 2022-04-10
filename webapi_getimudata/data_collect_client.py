from multiprocessing.sharedctypes import Value
import socketio
import os
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import threading
import numpy as np
import time
import json
import pandas as pd
from datetime import date
import sys
from os.path import dirname, join, abspath
import random
import time
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
current_folder_path = os.path.dirname(abspath(__file__))

## Gesture config
json_path = os.path.join(current_folder_path,'GESTURE_CONFIG.json')

with open(json_path,"r") as f:
    gesture_config = json.load(f)

gesture_main = gesture_config["main_gesture"]
main_repeat = gesture_config["main_repeat"]
main_duration = gesture_config["main_duration"]
flag_main = False

gesture_noise = gesture_config["noise_gesture"]
noise_repeat = gesture_config["noise_repeat"]
noise_duration = gesture_config["noise_duration"]
flag_noise = False

attribute = ["timestamp","acc_x","acc_y","acc_z","linearacc_x","linearacc_y","linearacc_z",
            "gyro_x","gyro_y","gyro_z","mag_x","mag_y","mag_z",
            "absori_x","absori_y","absori_z","absori_w","relori_x","relori_y","relori_z","relori_w","batch"]

attributeShort = ["timestamp","linearacc_x","linearacc_y","linearacc_z",
            "gyro_x","gyro_y","gyro_z","batch","interval"]

sensor_dataframe = pd.DataFrame(columns = attributeShort)

sio = socketio.Client()

flag_socket_start = 0
count_socket_datapoints = 0
sensor_list = {
    "timestamp": [],
    "linearacc_x":[],
    "linearacc_y":[],
    "linearacc_z":[],
    "gyro_x":[],
    "gyro_y":[],
    "gyro_z":[],
    "batch":[],
    "interval":[],
}

@sio.event
def connect():
    print('connection established')

@sio.on('sensor')
def my_message(data):
    print('message received with ', data)

@sio.event
def disconnect():
    print('disconnected from server')

@sio.on('count')
def on_message(c):
    global count_socket_datapoints
    if (count_socket_datapoints != c):
        print('not the same!!!',c-count_socket_datapoints)

@sio.on('sensor package')
def on_message(message):
    global flag_socket_start
    global sensor_dataframe
    global count_socket_datapoints
    #print(json.loads(message))
    
    count_socket_datapoints += 1
    if flag_socket_start == 0:
        pass
    if flag_socket_start == 1:
        # start loading data
        x = json.loads(message)

        # if (max(x["linearacc_z"]) > 5):
        #     print("action detected")

        sensor_list["timestamp"].extend(x["timestamp"])
        sensor_list["linearacc_x"].extend(x["linearacc_x"])
        sensor_list["linearacc_y"].extend(x["linearacc_y"])
        sensor_list["linearacc_z"].extend(x["linearacc_z"])
        sensor_list["gyro_x"].extend(x["gyro_x"])
        sensor_list["gyro_y"].extend(x["gyro_y"])
        sensor_list["gyro_z"].extend(x["gyro_z"])
        sensor_list["batch"].extend(x["batch"])
        sensor_list["interval"].extend(x["interval"])

def TIMER():
    """ A simple timer function to print clocking in terminal
    """

    global sensor_dataframe
    global flag_socket_start

    print('2')
    flag_socket_start = 1

    time.sleep(1)

    print('1')
    time.sleep(1)
    
    print('Start!\n')

    if (flag_main):
        duration = main_duration
    elif (flag_noise):
        duration = noise_duration
    else:
        raise ValueError("Flag main/noise is not correct!")

    for tick in range(duration,0,-1):
        print(f"Time Left: {tick}", end = "\n")
        time.sleep(1)
    print("")

    flag_socket_start = 0
    
    return

def record(gesture, repeat, path):
    """The record function given a gesture

    Args:
        gesture (str): gesture name
        repeat (int): total number of gesture repeat (for display purpose)
        path (str): path to save data
    """
    global sensor_dataframe
    global flag_socket_start
    global sensor_list

    loop_count = 0
    while (loop_count < repeat):
        print(f'\nThis is No. {loop_count + 1} / {repeat} time for the gesture: ||  {gesture}  || \n')
        prefix = ""
        if flag_main:
            prefix =  "GESTURE_"
        if flag_noise:
            prefix =  "NOISE_"
        filePath = os.path.join(path, prefix + f'{gesture}_{loop_count}.csv')

        while True:
            key = input('\nPress "y/1/enter" to start:\n')
            if (key != 'Y' and key != 'y' and key != 1 and key != "1" and key != ""):
                print("invalid input")
                continue
            else:
                break
        
        t = threading.Thread(target=TIMER,args=())
        t.start()
        t.join()

        flag_socket_start = 0
        while True:
            key = input('\nPress "y/1/enter" to confirm or "n/2" to discard :\n')
            if (key == 'Y' or key == 'y' or key == 1 or key == "1" or key == ""):
                sensor_dataframe = pd.DataFrame.from_dict(sensor_list)
                print(sensor_dataframe.shape[0])
                sensor_dataframe.to_csv(filePath,index = False)
                print('Nice job! Record done\n')
                sensor_list = {
                    "timestamp": [],
                    "linearacc_x":[],
                    "linearacc_y":[],
                    "linearacc_z":[],
                    "gyro_x":[],
                    "gyro_y":[],
                    "gyro_z":[],
                    "batch":[],
                    "interval":[]
                }
                loop_count += 1
                break
            elif (key == 'N' or key == 'n' or key == 2 or key == "2"):
                print('OK! Discard this record. Starting this round again... \n')
                sensor_list = {
                    "timestamp": [],
                    "linearacc_x":[],
                    "linearacc_y":[],
                    "linearacc_z":[],
                    "gyro_x":[],
                    "gyro_y":[],
                    "gyro_z":[],
                    "batch":[],
                    "interval":[]
                }
                break
            else:
                print("Invalid Input")

# Main Function

if __name__ == "__main__":
    sio.connect('http://localhost:5000')
    print('Connection success')

    timestmap = date.today().strftime('%Y-%m-%d-%H-%M-%S')

    user = str(input('\nPlease enter your ID: '))

    folder_path = os.path.join(current_folder_path, "..", 'data_from_phone', str(user)+"_"+timestmap)

    while True:
        if os.path.exists(folder_path):
            print('The User ID is already been taken, please enter another User ID')
            user = str(input('\nPlease enter your ID: '))
            folder_path = os.path.join(current_folder_path, "..", 'data_from_phone', str(user)+"_"+timestmap)
        else:
            break
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    print('\nHello!',f'\nYour ID is {user} \n')
    
    # update the global flag to control some setting
    flag_main = True
    flag_noise = False
    for idx, g in enumerate(gesture_main):
        print("--------------------------------------")
        print(f"|    Data Collection Stage  {str(idx + 1)}/{str(len(gesture_main))}    |")
        print("--------------------------------------")
        record(g, main_repeat, folder_path)

    # update the global flag to control some setting
    flag_main = True
    flag_noise = False
    for idx, g in enumerate(gesture_noise):
        print("--------------------------------------")
        print(f"|    Noise Collection Stage  {str(idx + 1)}/{str(len(gesture_noise))}    |")
        print("--------------------------------------")
        record(g, noise_repeat, folder_path)

    print("Thanks!")
    sio.disconnect()