import rekognition_function as rek

# variables
bucket = 'dt373bucket'
prefix = 'SebAmanPar'
region = 'us-east-1'
source_file = 'SebAmanPar/connor1.jpg'
#target_file = 'john_magufuli.jpg'  # file located in same directory as this script
target_file = "jo.jpg"


# list objects in bucket
object_names = rek.list_objects(bucket, prefix, region)
#print objects in bucket
# rek.print_objects(object_names)

# compare a single face in a target file to a single face in a source file
# face_matches = rek.compare_faces(bucket, source_file, target_file, region)
# print("Face matches: " + str(face_matches))

# if str(face_matches) == "1":
#     print("Face match found.")
# else:
#     print("No face match found.")


# compare a single face in a target file to all faces in source files

rek.compare_faces_all(bucket, prefix, target_file, region)    

