import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_operation(op_id):
    docs = db.collection('ai_operation').get()

    for doc in docs:
        # Extract the 'aiop_name' and 'aiop_id' from each dictionary
        aiop_name = doc.to_dict()['aiop_name']
        aiop_id = doc.to_dict()['aiop_id']

        # Print the extracted values
        #print(f"aiop_name: {aiop_name}, aiop_id: {aiop_id}")
        if op_id == aiop_id:
            return aiop_id


def get_id_of_cam(id_op):
    docs = db.collection('aiop_camera').get()

    for doc in docs:
        # Extract the 'aiop_id' and 'cam_id' from each dictionary
        aiop_id = doc.to_dict()['aiop_id']
        cam_id = doc.to_dict()['cam_id']

        # Print the extracted values
        #print(f"aiop_id: {aiop_id}, cam_id: {cam_id}")
        if id_op == aiop_id:
            return cam_id


def get_url_of_cam(url_of_cam):
    docs = db.collection('camera').get()

    for doc in docs:
        # Extract the 'aiop_name' and 'aiop_id' from each dictionary
        cam_id = doc.to_dict()['cam_id']
        cam_url = doc.to_dict()['cam_url']

        # Print the extracted values
        #print(f"cam_id: {cam_id}, cam_url: {cam_url}")
        if url_of_cam == cam_id:
            return cam_url


def get_id_of_obj(id_obj):
    docs = db.collection('aiop_obj').get()

    for doc in docs:
        # Extract the 'aiop_id' and 'cam_id' from each dictionary
        aiop_id = doc.to_dict()['aiop_id']
        obj_id = doc.to_dict()['obj_id']

        # Print the extracted values
        #print(f"aiop_id: {aiop_id}, obj_id: {obj_id}")
        if id_obj == aiop_id:
            return obj_id



def get_name_of_obj(id_name_of_obj):
    docs = db.collection('object').get()

    for doc in docs:
        # Extract the 'aiop_id' and 'cam_id' from each dictionary
        obj_id = doc.to_dict()['obj_id']
        obj_name = doc.to_dict()['obj_name']

        # Print the extracted values
        #print(f"obj_id: {obj_id}, obj_name: {obj_name}")
        if id_name_of_obj == obj_id:
            return obj_name
def  update_ws_url(ai_op_id,ws_url)  :
    #docs_ops = db.collection('ai_operation').get()
    # Udpdate:
    doc = db.collection(u'ai_operation').document(ai_op_id) # doc is DocumentReference
    field_updates = {"ws_url": ws_url}
    doc.update(field_updates)
    #city_ref = db.collection(u'ai_operation').document(u'ai_op_id')




if __name__ == "__main__":

   # id_of_op = get_operation('kNi2xun65eTAmu2M0Oua')

    id_of_op ='kNi2xun65eTAmu2M0Oua'
    update_ws_url( id_of_op,'yusyfstackoverflow.com/questions/54898304/google-firebase-get-update-or-create-documents-using-python')
    """
    print(id_of_op)
    id_of_cam = get_id_of_cam(id_of_op)
    print(id_of_cam)
    url_of_cam = get_url_of_cam(id_of_cam)
    print(url_of_cam)
    id_of_obj = get_id_of_obj(id_of_op)
    print(id_of_obj)
    name_of_obj = get_name_of_obj(id_of_obj)
    print(name_of_obj)

"""