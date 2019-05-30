class Athlete:
    def __init__(self, name, dob=None,times=[]):
        self.name=name
        self.dob=dob
        self.times=times


def sanitize(arr):
    speed=[]
    a = Athlete(arr.pop(0),arr.pop(0),[])
    for s in arr:
        clean_txt = str(s).replace(':','.').replace('-','.');
        if(clean_txt not in speed):
            speed.append(clean_txt)
    speed.sort()
    a.times=speed
    return a

try:
    with open("james2.txt","r") as james:
        arr=james.readline().strip().split(",")
except IOError as err:
    print(str(err))
ath = sanitize(arr)
print(ath.name)
print(ath.dob)
print(ath.times)

