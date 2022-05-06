import cv2, threading, queue

class ThreadingClass:
  # initiate threading class
  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)#return videos from our webcam
	# define an empty queue and thread
    self.q = queue.Queue()
    t = threading.Thread(target=self._reader)
    t.daemon = True#alwys the thread will be exicuted in bkgd so we will tell that to exit from main
    t.start()#internally it calls the run() method

  # read the frames as soon as they are available, discard any unprocessed frames;
  # this approach removes OpenCV's internal buffer and reduces the frame lag
  def _reader(self):
    while True:
      (ret, frame) = self.cap.read() # read the frames through camera and ---
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()#raise an empty exception if que empty
        except queue.Empty:
          pass
      self.q.put(frame) # --- store them in a queue (instead of the buffer)

  def read(self):
    return self.q.get() # fetch frames from the queue one by one
print("processed video frame successfully")