from importlib import import_module
import os
from flask import Flask, render_template, request, redirect, send_file, url_for, Response
from  ObjectDetection import * 
app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('test.html')




@app.route('/aiop_id',methods=['GET'])
def operation_start():
    print(' operation_start  dxfgsdf')
    """Video streaming route. Put this in the src attribute of an img tag."""
    #http.get(uri,headers: {'aiop_id':aiop_id})   
    aiop_id_var = request.args.get('aiop_id')
    print(' id from request ')
    print(aiop_id_var)
    satrt_video(aiop_id_var)
    return Response()
@app.route('/aiop_id_stop',methods=['GET'])
def stop_video():
    print(' operatoion is starting to stop ')
    """Video streaming route. Put this in the src attribute of an img tag."""
    aiop_id_var = request.args.get('aiop_id_stop')
    print(' id from request ')
    print(aiop_id_var)
    stop_videoDB(aiop_id_var)
    return Response()
    import ObjectDetection
    ObjectDetection.stop_video()
    return Response()
                  

          


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, port=5001)
