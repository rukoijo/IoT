import boto3

# function to list objects in a bucket
def list_objects(bucket, prefix, region):
    """returns a list of objects in a bucket as strings """
    client = boto3.client('s3', region_name=region)
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    
    object_names = [obj['Key'] for obj in response.get('Contents', [])]
    
    return object_names[1:]

# function to print objects in a bucket
def print_objects(object_names):
    """prints the objects in a bucket"""
    print("Objects in the specified directory:")
    for obj in object_names:
        print(obj)

# function to compare one target image in local drive to one source images in bucket
def compare_faces(bucket, sourceFile, targetFile, region):
    client = boto3.client('rekognition', region_name=region)

    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'S3Object': {
                                        'Bucket': bucket, 'Name': sourceFile}},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + similarity + '% confidence')

    imageTarget.close()
    return len(response['FaceMatches'])

# function to compare one target image in local drive to all source images in bucket
def compare_faces_all(bucket, prefix, targetFile, region):
    client = boto3.client('rekognition', region_name=region)

    # imageTarget = open(targetFile, 'rb')

    objects = list_objects(bucket, prefix, region)
    print_objects(objects)

    face_matches = 0

    for obj in objects:
        print("Bucket: %s, Source: %s, Target: %s, region: %s" % (bucket, obj, targetFile, region))
        response = compare_faces(bucket, str(obj), targetFile, region )


        # for faceMatch in response['FaceMatches']:
        #     position = faceMatch['Face']['BoundingBox']
        #     similarity = str(faceMatch['Similarity'])
        #     print(f'The face in {sourceFile} matches with {similarity}% confidence in {obj}')

        face_matches += response
        if response > 0:
            print("Face match found.", obj)

    # imageTarget.close()
    return face_matches




