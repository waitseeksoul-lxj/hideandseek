import Crypto.Cipher.AES
import Crypto.Hash.SHA
import random
import cPickle
import pickle
import string
import base64


rnd = random.Random()
base_hash = Crypto.Hash.SHA.new("Mosso's Secret").digest()

class AesWrapperException:
    pass

class MsgTooBig(AesWrapperException):
    def __repr__(self):
        return "Msg to big for encryption"

class InvalidKey(AesWrapperException):
    def __repr__(self):
        return "EncryptionKey/DecryptionKey don't match"

class UnknownPickleMethod(AesWrapperException):
    def __repr__(self):
        return "Unknown pickle method"

class Aes_wrapper(object):
  def __init__(self,key_in,len_bytes=4):
    self.key = Crypto.Hash.SHA.new(key_in).digest()[0:16]
    self.aes = Crypto.Cipher.AES.new(self.key)
    self.len_bytes = len_bytes
    self.max_size = 2**(len_bytes*8) - 1
    self.len_nibbles = len_bytes * 2

  def dumps(self,obj,**kw):
      if "method" in kw:
          if kw["method"] == "pickle":
              pdump = pickle.dumps(obj)
          elif kw["method"] == "cpickle":
              pdump = cPickle.dumps(obj)
          else:
              raise UnknownPickleMethod
              return Nonw
      else:
          pdump = cPickle.dumps(obj) #use pickle by default

      cdump = self.encrypt(pdump)
      return cdump

  def loads(self,cdump,**kw):
      pdump = self.decrypt(cdump)

      if "method" in kw:
          if kw["method"]=="cpickle":
              obj = cPickle.loads(pdump)
              return obj
          elif kw["method"]=="pickle":
              obj = pickle.loads(pdump)
              return obj
          else:
              raise UnknownPickleMethod
              return None
      else:
          obj = cPickle.loads(pdump)
          return obj

     
  def dump(self,obj,fp,**kw):
      cdump = self.dumps(obj,**kw)
      fp.write(cdump)
      fp.close()

  def load(self,fp,**kw):
      cdump = fp.read()
      obj = self.loads(cdump,**kw)
      return obj

  def load_file(self,file_name,**kw):
      path = os.path.expanduser(file_name)
      fp = open(path,"r")
      obj = self.load(fp,**kw)
      fp.close()
      return obj

  def save_file(self,obj,file_name,**kw):
      path = os.path.expanduser(file_name)
      fp = open(path,"w")
      self.dump(obj,fp,**kw)
      fp.close()

  def encrypt(self,msg_in):
    if len(msg_in)>self.max_size:
      raise MsgTooBig
      return None
    length   = hex(len(msg_in))[2:]
    msg_out  = base_hash
    msg_out += pad(self.len_nibbles,'0',length)
    msg_out += msg_in
    while len(msg_out)%16 != 0:
      msg_out += " "
    ctext = self.aes.encrypt(msg_out)
    return ctext

  def decrypt(self,cmsg):
    lnibbles = self.len_nibbles
    hash_in = self.aes.decrypt(cmsg)[:len(base_hash)]
    if hash_in != base_hash:
        raise InvalidKey
    ptext   = self.aes.decrypt(cmsg)[len(base_hash):]
    try:
      length  = int(ptext[0:lnibbles],16)
    except:
      return None
    msg_out = ptext[lnibbles:lnibbles+length]
    return msg_out

  def b64encrypt(self,msg_in):
    ctext = base64.standard_b64encode(self.encrypt(msg_in))
    return ctext

  def b64decrypt(self,cmsg):
    ptext = self.decrypt(base64.standard_b64decode(cmsg))
    return ptext

def random_iv(nch):
    return string.join([chr(rnd.randint(0,255)) for x in xrange(0,nch)],"")


def aes_encrypt(ptext,key):
    aes = Aes_wrapper(key,len_bytes=2)
    iv = random_iv(4)
    msg = iv + ptext
    ctext = aes.encrypt(msg)
    return ctext

def aes_decrypt(ctext,key):
    aes = Aes_wrapper(key,len_bytes=2)
    msg = aes.decrypt(ctext)
    ptext = msg[4:]
    return ptext

def aes_b64encrypt(ptext,key):
    aes = Aes_wrapper(key,len_bytes=2)
    iv = random_iv(4)
    msg = iv + ptext
    ctext = aes.b64encrypt(msg)
    return ctext

def aes_b64decrypt(ctext,key):
    aes = Aes_wrapper(key,len_bytes=2)
    msg = aes.b64decrypt(ctext)
    ptext = msg[4:]
    return ptext

def b64decode(str_in):
    str_out = base64.standard_b64decode(str_in)
    return str_out

def b64encode(str_in):
    str_out = base64.standard_b64encode(str_in)
    return str_out

def pad(digits,ch,val,**kargs):
  str_out=str(val)
  if not "side" in kargs:
    kargs["side"]="LEFT_DIR"
  if kargs["side"]=="LEFT_DIR":
    for i in xrange(0,digits-len(str_out)):
      str_out = ch + str_out
    return str_out
  if kargs["side"]=="RIGHT_DIR":
    for i in xrange(0,digits-len(str_out)):
      str_out = str_out + ch
    return str_out

