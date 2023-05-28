def CreateNewAdmin(Collection,uname,passw,admin):
    print(uname,"this is the New User")
    Collection.insert_one(
        {
            "Uname": uname,
            "passw" : passw,
            "addedby" : admin
        })
    print("New Admin Created Successfully!!")

def getUserDet(Collection,name,passw):
    val = {}
    det = Collection.find({
        "Uname" : name,
        "passw" : passw
    })
    for i in det:
        print("the type is :",type(i["Uname"]))
        val['uname'] = i["Uname"]
        val['passw'] = i["passw"]
        val['addedby'] = i["addedby"]
    return val
