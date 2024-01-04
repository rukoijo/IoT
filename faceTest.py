import boto3

def list_objects(bucket, region):
    client = boto3.client('s3', region_name=region)
    response = client.list_objects_v2(Bucket=bucket)
    return [obj['Key'] for obj in response.get('Contents', [])]

# def compare_faces(bucket, sourceFile, targetFile, region):
#     client = boto3.client('rekognition', region_name=region)

#     target_image = open(targetFile, 'rb').read()

#     objects = list_objects(bucket, region)

#     face_matches = 0

#     for obj in objects:
#         response = client.compare_faces(
#             SimilarityThreshold=99,
#             SourceImage={'S3Object': {'Bucket': bucket, 'Name': sourceFile}},
#             TargetImage={'Bytes': target_image}
#         )

#         for faceMatch in response['FaceMatches']:
#             position = faceMatch['Face']['BoundingBox']
#             similarity = str(faceMatch['Similarity'])
#             print(f'The face in {sourceFile} matches with {similarity}% confidence in {obj}')

#             face_matches += 1

#     return face_matches

bucket = 'dt373bucket'
source_file = 'SebAmanPar/john_magufuli.jpg'
target_file = 'john_magufuli.jpg'
region = "us-east-1"

#face_matches = compare_faces(bucket, source_file, target_file, region)

#print(f"Total face matches: {face_matches}")

#if face_matches > 0:
#    print("Face match(es) found.")
#else:
#    print("No face match found.")

print(list_objects(bucket, region))
