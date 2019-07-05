import random
import datetime
import uuid



def random_string(string_length):
    random=str(uuid.uuid4())
    random=random.upper()
    random=random.replace("-","")
    return random[0:string_length]



def temps():
  while True:
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    idt = str(random_string(9))

    temp = str(random.uniform(0.0,50.0))

    msg = idt + ";" + ts + ";" + temp + "\n"

    print(msg)

    return msg

