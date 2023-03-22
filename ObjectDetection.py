import asyncio
from os import getpid, kill
from signal import SIGKILL
import websockets
import base64
import cv2
import torch
from Tracker import *
import numpy as np
from threading import Thread
import database 
import dependencies.pafy as pafy

model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)
basic_url='143.244.138.22'
#basic_url='127.0.0.1'
# green area
area_1 = [(30, 40), (30, 460), (620, 460), (620, 40)]


def points(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)


async def send_data(websocket, video1_path):
    counter1 = set()
    tracker1 = Tracker()

    cap1 = cv2.VideoCapture(video1_path)
    objects_to_count = ["person", "car"]

    async def send_video(cap, counter, tracker):
        while True:
            if stopthread :
                break
            # Read an image from the camera
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (640, 480))
            cv2.polylines(frame, [np.array(area_1, np.int32)], True, (0, 255, 255), 3)
            results = model(frame)
            list = []

            for index, row in results.pandas().xyxy[0].iterrows():
                x1 = int(row["xmin"])
                y1 = int(row["ymin"])
                x2 = int(row["xmax"])
                y2 = int(row["ymax"])
                obj_name = row["name"]
                if obj_name in objects_to_count:
                    list.append([x1, y1, x2, y2])
            boxes_ids = tracker.update(list)
            for box_id in boxes_ids:
                x, y, w, h, id = box_id
                cv2.rectangle(frame, (x, y), (w, h), (255, 0, 255), 2)
                cv2.putText(
                    frame, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2
                )
                result = cv2.pointPolygonTest(
                    np.array(area_1, np.int32), (int(w), int(h)), False
                )
                if result > 0:
                    counter.add(id)
            p = len(counter)
            cv2.putText(
                frame, str(p), (20, 30), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2
            )

            # Convert the image to a JPEG byte string
            ret, buffer = cv2.imencode(".jpg", frame)
            jpg_as_text = base64.b64encode(buffer).decode("utf-8")
            # Send the image and the p value over the websocket
            message = f"{p},{jpg_as_text}"
            await websocket.send(message)
            # Wait for some time before sending the next image
            await asyncio.sleep(0.01)
            

        cap.release()
        cv2.destroyAllWindows()

    # Run the two video capture loops asynchronously
    await asyncio.gather(send_video(cap1, counter1, tracker1))




#def stop_operatio_detection( operationid) :



#def start_operatio_detection( operationid) :

pool = { }

# thisdict.update({"codfhgdfghdfghdflor": thread1})









async def start_server(video_path, port):
    # Create a new VideoCapture object
    if "youtube" in video_path:
        video = pafy.new(video_path)
        best = video.getbest()
        video_path = best.url
    async with websockets.serve(
        lambda websocket: send_data(websocket, video1_path=video_path),
        basic_url,
        port,
    ):
        await asyncio.Future()


# Create two threads for running the servers


def stop_videoDB(aiop_id):   
    pid = getpid()
    kill(pid, SIGKILL)


#thread2 = Thread(target=lambda: asyncio.run(start_server("vb.m4v", 8766)))
def satrt_video(aiop_id_var):
    # get  operation Infomation  URL camera information from DB
    id_of_cam = database.get_id_of_cam(aiop_id_var)
    print(id_of_cam)
    #port = generate_port();
    import random
    number = random.randint(1000,9999)
    print(number)
    port=number
   # ws://localhost:8766/
    database.update_ws_url(aiop_id_var,'ws://'+basic_url+':'+str(port))
    url_of_cam = database.get_url_of_cam(id_of_cam)
    thread1 = Thread(target=lambda: asyncio.run(start_server(url_of_cam, port)))
    thread1.start()
    thread1.join()
    
#StoppableThread(thread1)
stopthread = False
if __name__ == "__main__":
    # Start the threads
   # thread1.start()
    # print(thread1.native_id )
# get the pid of the current process
    pid = getpid()
# report a message
   # print(f'Running with pid: {pid}')
   # kill(pid, SIGKILL)
    #thread2.start()
    # Wait for the threads to complete
   # thread1.join()
   # thread2.join()


