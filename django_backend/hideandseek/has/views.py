# Create your views here.

from django.template import Context
from django.db.models import Q
import json

import hideandseek.has
import new

class DynamicLoader(object):
    def __init__(self):
        self.mod_dict = {}

    def abs_import(self,mod_path):
        if not self.mod_dict.has_key(mod_path):
            print "Trying to import :",mod_path
            mod = __import__(mod_path)

            for sub_module in mod_path.split(".")[1:]:
                mod = getattr(mod,sub_module)
            self.mod_dict[mod_path] = mod
        return self.mod_dict[mod_path]

    def keys():
        return mod_dict.keys()

class HView(object):
    def __init__(self):
        self.dl = DynamicLoader()
        dl = self.dl
        
        meth_dict = {"hideandseek.has.view.test":
                       ["jsonout","jsonin","avgpoints"]
                    }
        for (mod_name,method_names) in meth_dict.items():
            for meth_name in method_names:
                mod = dl.abs_import(mod_name)
                meth_def = getattr(mod,meth_name)
                new_method = new.instancemethod(meth_def,self,self.__class__)
                setattr(self,meth_name,new_method)

    #load json object from request
    def loadJson(self):
        return json.loads(self.request.raw_post_data)

#Generic view
    def gview(self,request,*args,**kw):
        if "view" in kw:
            view_name = kw["view"]
            func = getattr(self,"%s"%view_name)
            self.request = request
            self.session = request.session
            self.raw = request.raw_post_data
            self.ctx = Context()
            self.jdumps = json.dumps
            self.jloads = json.loads
            return func()
