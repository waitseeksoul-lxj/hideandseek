import cPickle
import string
import json
import os

def save_cpickle(obj,file_name):
    ignoreCtrlC = True
    data = cPickle.dumps(obj)
    file_path = os.path.expanduser(file_name)
    while ignoreCtrlC:
       try:
           open(file_path,"w").write(data)
           break
       except (KeyboardInterrupt,SystemExit):
           printf("KeyPress Ignored\n")
           continue
    return None

def load_cpickle(file_name):
    file_path = os.path.expanduser(file_name)
    data = open(file_path,"r").read()
    obj = cPickle.loads(data)
    return obj

def load_json(file_name):
    file_path = os.path.expanduser(file_name)
    fp = open(file_path,"r")
    jtext = fp.read()
    fp.close()
    obj = json.loads(jtext)
    return obj

def save_json(obj,file_name):
    file_path = os.path.expanduser(file_name)
    try:
        jtext = json.dumps(obj,indent=2)
    except:
        printf("Error %s\n",traceback.format_exc())
        sys.exit()
    fp = open(file_path,"w")
    fp.write(jtext)
    fp.close()

