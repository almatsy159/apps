import time

prfx = f"   #BEG OF {__name__} at {time.time()}"
sfx = f"    #END OF{ __name__} "
def output(data="",prfx=prfx,sfx=sfx):
    try:
        with open("static/output.txt","w+") as f:
            f.write(f"\n{prfx}")
            f.write(f"\n{data}\n")
            f.write(f"{sfx}\n")
            
    except:
        print("couldn't write in file\n",data)
    