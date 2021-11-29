#### Requirement 
- for arm64 (Jetson Nano ,AGX Xavire)

see: (https://github.com/jkjung-avt/tensorrt_demos)

#### YOLO
1. requires TensorRT 6.x+.
    - You could check which version of TensorRT has been installed on your Jetson system by looking at file names of the libraries.
```
ls /usr/lib/aarch64-linux-gnu/libnvinfer.so*
```
![alt text](https://github.com/NMB-MIC/utils/blob/main/jetson/tensorrt/setup/tensorrt_check_version.JPG)
2.  create project dir and clone tensorrt_demos
```
mkdir project &&
cd project &&
git clone https://github.com/jkjung-avt/tensorrt_demos.git 
```
3. install pycuda
```
cd ${HOME}/project/tensorrt_demos/ssd
./install_pycuda.sh
```
4. install onnx(require protobuf)
```
sudo pip3 install onnx==1.4.1
```
5. make
``` 
cd ${HOME}/project/tensorrt_demos/plugins &&
make
```
6. download pretrain models and convert to tensorrt
```
cd ${HOME}/project/tensorrt_demos/yolo &&
./download_yolo.sh &&
python3 yolo_to_onnx.py -m yolov4-416 &&
python3 onnx_to_tensorrt.py -m yolov4-416

```
7. Test the TensorRT "yolov4-416" engine with the "dog.jpg" image.
```
cd ${HOME}/project/tensorrt_demos &&
wget https://raw.githubusercontent.com/pjreddie/darknet/master/data/dog.jpg -O ${HOME}/Pictures/dog.jpg &&
python3 trt_yolo.py --image ${HOME}/Pictures/dog.jpg \
                      -m yolov4-416
```