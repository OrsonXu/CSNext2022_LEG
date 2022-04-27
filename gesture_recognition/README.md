# Collect data from a phone's accelerometer and gyroscope

## Envionment Setup

Please open three terminals (that's a lot!) and run one of the following three commands in each terminal in the same order.

1. Start a local server that hosts a website and opens port 5000
```
python server.py
```

2. Expose the local port to public website
```
ngrok http 5000
```

After running this, this terminal will look different and display things like (each time the http/https links are random and unqiue):

```
Session Status     online
Account            orson.xuhai.xu@gmail.com (Plan: Free)
Update             update available (version 2.3.40, Ctrl-U to update)
Version            2.3.35
Region             United States (us)
Web Interface      http://127.0.0.1:4040
Forwarding         http://22d2-205-175-97-234.ngrok.io -> http://localhost:5000
Forwarding         https://22d2-205-175-97-234.ngrok.io -> http://localhost:5000
Connections        ttl     opn     rt1     rt5     p50     p90
                   0       0       0.00    0.00    0.00    0.00
```

3. Start another local client that waits for signals sent from the server.

```
python data_collect_client.py
```

You can then follow the texts in the terminal to enter a `user_id` that can identify this round of data collection. The data will be saved in `data_from_phone/[your user_id]`.

Stop before actual data collection. You can resume after the Phone setup (see below).

Please read `data_collect_client.py` for more details. 


## Phone Setup

On the phone, use Chrome (for android) or Safari (for iOS) to go to the following link:

```
[https url shown by the nrgok]/phone
```

In the example above, you will visit

```
https://22d2-205-175-97-234.ngrok.io/phone
```

You will see a page like this.
- If you are an Android user, just click on the first button, the data will be sent to the server.
- If you are an iOS user, click on the third button to obtain the permission, and then click on the first button, the data will be sent to the server.

Once the data is being sent to the server in real-time, you can go back to the third terminal and start the data collection process and have fun :)

<img src="figures/website.jpeg" alt="My cool logo"  width="300"/>



## We need to put the phone in the pocket...

However, in the actual data collection process, the phone will need to be put in the pocket, which may cause a lot of unwanted clicks. Meanwhile, we cannot leave the browser app as this would pause the data collection.

We need to find some workaround!

### For Android

Download an app like `Touch Lock` to lock the screen after the data is being sent to the server.

### For iOS

Follow [this tutorial](https://beebom.com/how-disable-touchscreen-on-iphone-and-ipad/#:~:text=To%20do%20so%2C%20make%20sure,Guided%20Access%20with%20Face%20ID.) to turn on the `Guided Access` features on iPhone, which is capable of disabling screen touch.