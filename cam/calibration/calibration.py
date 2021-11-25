class Distrosion(QThread):
change_pixmap_signal = pyqtSignal(np.ndarray)

def __init__(self,parent=None):
super(Distrosion, self).__init__(parent)
self.Info = "Camera"
self.mtxMain , self.distMain = self.load_coefficients('./data/Master_Model/calibration_chessboard.yml')

def calibrate_chessboard(self,dir_path, image_format, square_size, width, height):
'''Calibrate a camera using chessboard images.'''
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(8,6,0)
objp = np.zeros((height*width, 3), np.float32)
objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)

objp = objp * square_size

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = pathlib.Path(dir_path).glob(f'*.{image_format}')
# Iterate through all images
for fname in images:
img = cv2.imread(str(fname))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find the chess board corners
ret, corners = cv2.findChessboardCorners(gray, (width, height), None)

# If found, add object points, image points (after refining them)
if ret:
objpoints.append(objp)

corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
imgpoints.append(corners2)

# Draw and display the corners
cv2.drawChessboardCorners(img, (7,6), corners2, ret)
cv2.imwrite("Result calibration.png",img)
self.change_pixmap_signal.emit(img)



# Calibrate camera
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

return [ret, mtx, dist, rvecs, tvecs]
def save_coefficients(self,mtx, dist, path):
'''Save the camera matrix and the distortion coefficients to given path/file.'''
cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_WRITE)
cv_file.write('K', mtx)
cv_file.write('D', dist)
# note you *release* you don't close() a FileStorage object
cv_file.release()

def load_coefficients(self,path):
'''Loads camera matrix and distortion coefficients.'''
# FILE_STORAGE_READ
cv_file = cv2.FileStorage(path, cv2.FILE_STORAGE_READ)

# note we also have to specify the type to retrieve other wise we only get a
# FileNode object back instead of a matrix
camera_matrix = cv_file.getNode('K').mat()
dist_matrix = cv_file.getNode('D').mat()

cv_file.release()
return [camera_matrix, dist_matrix]

def start(self,name):
# from chessboard import calibrate_chessboard
# from utils import load_coefficients, save_coefficients

# Parameters
IMAGES_DIR = './pose/sample_image/'
IMAGES_FORMAT = 'png'
SQUARE_SIZE = 2
WIDTH = 6
HEIGHT = 9
self.name = name

# Calibrate
ret, mtx, dist, rvecs, tvecs = self.calibrate_chessboard(
IMAGES_DIR,
IMAGES_FORMAT,
SQUARE_SIZE,
WIDTH,
HEIGHT)
# Save coefficients into a file
self.save_coefficients(mtx, dist, "./data/Calibration_Model/"+str(name)+".yml")
msg = QMessageBox()
msg.setWindowTitle("SP VISION")
msg.setIcon(QMessageBox.Information)
msg.setText("Calibration Done")
msg.exec_()
def undistorsion(self,Image,name):
Path = "./data/Calibration_Model/"+str(name)+".yml"
self.mtxMain , self.distMain = self.load_coefficients(Path)
dst = cv2.undistort(Image, self.mtxMain, self.distMain, None, None)
return dst