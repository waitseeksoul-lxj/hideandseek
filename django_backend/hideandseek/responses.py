from django.http import HttpResponse

import json
import copy

class JsonResponse(HttpResponse):
    defaultVals = {"status":200,
                   "content_type":"application/json"}

    def __init__(self,*args,**kw):
        self.setDefaults(self.defaultVals,kw)        
        if not kw.has_key("entity"):
            raise KeyError("ResponseObjects require an entity")
        if not kw.has_key("content"):
            kw["content"] = json.dumps(kw["entity"],indent=2)
        del kw["entity"]
        HttpResponse.__init__(self,*args,**kw)

    def setDefaults(self,defaultVals,kw):
        for (k,v) in defaultVals.items():
            if not kw.has_key(k):
                kw[k]=v
        

class BadRequest(JsonResponse):
    defaultVals = {"status":200,
                   "content_type":"application/json"}

    def __init__(self,*args,**kw):
        self.setDefaults(self.defaultVals,kw)
        errormsg = "BadRequest"
        if kw.has_key("errormsg"):
            errormsg = kw["errormsg"]
            del kw["errormsg"]
        kw["entity"]={"Error":errormsg}
        JsonResponse.__init__(self,*args,**kw)
    
