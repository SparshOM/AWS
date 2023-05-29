import boto3
from multiprocessing.pool import ThreadPool as Pool
# from multiprocessing import Pool
from random import randint
from time import sleep
import os



def process_line(l):
    try:
        int(l)

        cmd="""aws s3 rm s3://sparshtest/"""+str(l).strip('\n')+"""/ s3://sparshtest/"""+str(l).strip('\n')+"""/ --recursive  """
        #print(cmd)
        os.system(cmd)
        

    except ValueError:
        print(l,"error")
        pass


def get_next_line():
    with open("crypt.csv", 'r') as f:
        for line in f:
            yield line

f = get_next_line()

t = Pool(processes=50)

for i in f:
    t.map(process_line, (i,))
t.close()
t.join()      
