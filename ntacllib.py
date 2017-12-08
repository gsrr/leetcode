# getntacl and setntacl script
import sys
import os
import copy
from samba.samba3 import param as s3param
from samba.dcerpc import security
from samba.samba3 import smbd


def getntacl_util(path):
    s3conf = s3param.get_context()
    s3conf.load("/etc/samba/smb.conf")
    sd = smbd.get_nt_acl(path, security.SECINFO_OWNER | security.SECINFO_GROUP | security.SECINFO_DACL | security.SECINFO_SACL, service=None)
    return sd

def getntacl(path, sddl = None):
    sd = getntacl_util(path)
    print type(sd.dacl.aces)
    for i in xrange(len(sd.dacl.aces)):
        print "type:", "%x"%sd.dacl.aces[i].type
        print "flags:", "%x"%sd.dacl.aces[i].flags
        print "access_mask:", "%x"%sd.dacl.aces[i].access_mask
        print "uid:", sd.dacl.aces[i].trustee.sub_auths
    return sd.as_sddl()

def setntacl_chown(path):
    sd = security.descriptor.from_sddl(sddl, security.dom_sid())
    print sd.owner_sid

IFT_SUBFOLDER = 0x0002
IFT_FILES     = 0x0001       
IFT_INHERITED = 0x0003

def separate_sd(sd):
    faces = []
    daces = []
    for i in xrange(len(sd.dacl.aces)):
        flags = sd.dacl.aces[i].flags
        if flags & IFT_FILES != 0:
            faces.append(sd.dacl.aces[i])
        daces.append(sd.dacl.aces[i])
    print faces
    print daces
    return faces, daces

def get_update_aces(sd, new_sd):
    aces = []
    for i in xrange(len(sd.dacl.aces)):
        flags = sd.dacl.aces[i].flags
        if flags & IFT_INHERITED == 0:
            aces.append(sd.dacl.aces[i])
    
    for i in xrange(len(new_sd.dacl.aces)):
        print new_sd.dacl.aces[i].flags
        new_sd.dacl.aces[i].flags |= IFT_INHERITED
        aces.append(new_sd.dacl.aces[i])
    return aces 

def setntacl_recur(rootpath, new_sd):
    print rootpath
    sd = getntacl_util(rootpath)   
    aces = get_update_aces(sd, new_sd)
    sd.dacl.aces = aces
    print "before"
    smbd.set_nt_acl(rootpath, security.SECINFO_OWNER | security.SECINFO_GROUP | security.SECINFO_DACL | security.SECINFO_SACL, sd, service = None)
    print "after"
    if os.path.isfile(rootpath) == True:
        return {'status' : 0}

    for subdir, dirs, files in os.walk(rootpath):
        faces, daces = separate_sd(sd)
        sd.dacl.aces = faces
        for f in files:
            fpath = subdir + os.sep + f
            print "fpath", fpath
            setntacl_recur(fpath, sd)
        '''
        sd.dacl.aces = daces
        for d in dirs:
            dpath = subdir + os.sep + d
            setntacl_recur(dpath, sd)
        '''
    return {'status' : 0}

def setntacl(rootpath, sddl):
    print rootpath
    s3conf = s3param.get_context()
    s3conf.load("/etc/samba/smb.conf")
    sd = security.descriptor.from_sddl(sddl, security.dom_sid())
    smbd.set_nt_acl(rootpath, security.SECINFO_OWNER | security.SECINFO_GROUP | security.SECINFO_DACL | security.SECINFO_SACL, sd, service = None)
    for subdir, dirs, files in os.walk(rootpath):
        faces, daces = separate_sd(sd)
        '''
        sd.dacl.aces = faces
        for f in files:
            fpath = subdir + os.sep + f
            setntacl_recur(fpath, sd)
        '''
        sd.dacl.aces = daces
        for d in dirs:
            dpath = subdir + os.sep + d
            setntacl_recur(dpath, sd)
    return {'status' : 0}

def main():
    if sys.argv[1] == "getntacl":
        print getntacl(sys.argv[2])
    else:
        setntacl(sys.argv[2], sys.argv[3])
    
if __name__ == "__main__":
    main()