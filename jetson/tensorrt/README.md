#### Requirement 
- for arm64 (Jetson Nano ,AGX Xavire)

see: (https://github.com/jkjung-avt/tensorrt_demos)

#### YOLO
1. requires TensorRT 6.x+.
    - You could check which version of TensorRT has been installed on your Jetson system by looking at file names of the libraries.
```
ls /usr/lib/aarch64-linux-gnu/libnvinfer.so*
```
![alt text](https://github.com/NMB-MIC/utils/blob/main/jetson/tensorrt/tensorrt_check_version.JPG)
2.  create project dir and clone tensorrt_demos
```
mkdir project &&
cd project &&
git clone https://github.com/jkjung-avt/tensorrt_demos.git 
```
3. Install pycuda
```
cd ${HOME}/project/tensorrt_demos/ssd
./install_pycuda.sh
```


