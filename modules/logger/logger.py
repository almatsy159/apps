import time

prfx = f" at {time.time()} beg of :\n"
sfx = f"\n  END \n"
def output(data="",def_path="static/output.txt",mode="w",prfx=prfx):
    try:
        with open(def_path,mode=mode) as f:
            f.write(prfx)
            f.write(f"\n{data}\n")
            f.write(sfx)
            
    except FileNotFoundError as err:
        print(err)
    