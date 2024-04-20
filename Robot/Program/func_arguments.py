


def name(*args,**kwargs):                              #  *args can take any number of arguments. We can update the arguments
    for i in args:
        print(i)                                       # Argument name can be anything. We can write *a instead of *args

    for i in kwargs.values():                          # **kwargs is used when we have dictionary object as argument
        print(i)

list=["Gaurav","Archii","Shekhar","Radhika","Anita"]


dict={"First":"Aman","Second":"Ankit","Third":"Kapil"}
name(*list,**dict)
