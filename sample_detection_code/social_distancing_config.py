# base path to YOLO directory
MODEL_PATH = "yolo-coco"
# initialize minimum probability to filter weak detections along with
# the threshold when applying non-maxima suppression
MIN_CONF = 0.3
NMS_THRESH = 0.3
People_Counter = True #to count people
Threshold = 15 #threshold value
url = 0 #to open our web cam
ALERT = True #if there is a violation then alert to specified email
MAIL = 'aneettathomas1212@gmail.com'
USE_GPU = False #if we need graphic processing unit instead of cpu
MAX_DISTANCE = 80
MIN_DISTANCE = 50
#for testing
print(Threshold)
print(url)
print(ALERT)
print(MAIL)
print(USE_GPU)
print(MAX_DISTANCE)
print(MIN_DISTANCE)

