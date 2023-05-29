import boto3
import json
import sys 

def check_s3_key_type(bucket_name, key):
    key=key.rstrip(key[-1])
   
    s3 = boto3.client('s3',aws_access_key_id= '****************',aws_secret_access_key='*************************************')
    
    try:
        response = s3.head_object(Bucket=bucket_name, Key=key)
        # If there is no error, the key represents an object
        #print("Stp-1"+key)
    except s3.exceptions.ClientError as e:
        # If there is an error, the key might represent a folder
        error_code = e.response['Error']['Code']
        if error_code == '404':
            list_s3_folders(bucket_name,1,key)
            #print(key)
        else:
            print(error_code)
            # Handle other errors if necessary
            pass

def list_s3_folders(bucket_name, limit, folder):
    d=0

    s3 = boto3.client('s3',aws_access_key_id= ''****************',',aws_secret_access_key='='*************************************')')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=str(folder)+"/", Delimiter='/')

    folders = []
    while True:
        if 'CommonPrefixes' in response:
            folders.extend(response['CommonPrefixes'])
        #print(len(folders))
        if len(folders)==0:
            response_detail = s3.list_objects_v2(Bucket=bucket_name, Prefix=str(folder)+"/",MaxKeys=1)
            print(folder)
            folder1=folder.rstrip(folder[-1])
            response_video = s3.list_objects_v2(Bucket=bucket_name, Prefix=str(folder1)+"V/", Delimiter='/')
            #print(response_video)
            d=1
            #print(response_detail)
        if d==1:
            if 'Contents' in response_detail:
                for obj in response_detail['Contents']:
                    
                    print("<h4> Last Modified:<span style='color:red'>"+str(obj['LastModified'])+"</span></h4>")
                    print("<h4> Storage Type:<span style='color:red'>"+str(obj['StorageClass'])+"</span></h4>")
            if 'Contents' in response_video:
                
                print("<h4> Video: <span style='color:red'>Available</span></h4>")
        if 'NextContinuationToken' in response and len(folders) < limit:
            response = s3.list_objects_v2(Bucket=bucket_name, Prefix=str(folder)+"/", Delimiter='/', ContinuationToken=response['NextContinuationToken'])
        else:
            #print(response)
            break
    
    folder_new= folders[:limit]
    for folder in folder_new:
        #print(folder['Prefix'])
        check_s3_key_type(bucket_name,folder['Prefix'])

# Example usage
bucket_name = 'ucanassessm'
limit = 1
#folder = '7616841296871/'
after_json = sys.argv[1]
after_json=after_json[1:-1].split("|")

folder=after_json[0]+"/"
print("<h3> Crypt Id:"+folder+"</h3><br/>")

check_s3_key_type(bucket_name,folder)
#folders = list_s3_folders(bucket_name, limit, folder)
#for folder in folders:
#print(folder['Prefix'])