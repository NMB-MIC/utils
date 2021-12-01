
#### Requirement 
- for arm64 (AGX Xavire)

see: (https://github.com/jetsonhacks/installROSXavier)
(https://www.youtube.com/watch?v=HjFs00rrJfY)


#### How to install ros workspace
1. requires qt5
```
sudo apt-get install qtbase5-dev
sudo apt-get install qtdeclarative5-dev
```
2. git clone
```
git clone https://github.com/jetsonhacks/installROSXavier.git
```
3. install ros-melodic-desktop
```
./installROS.sh -p ros-melodic-desktop
```
4. create workspace
```
./setupCatkinWorkspace.sh
```
5. edit ip address
```
gedit ~/.bashrc
```
![alt text](https://github.com/NMB-MIC/utils/blob/main/jetson/dobot/ros/edit_ip.JPG)
6. check program complete
- open new terminal
```
cd catkin_ws &&
source devel/setup.bash &&
rostopic list
```


#### How to install ros workspace
(see: https://github.com/Dobot-Arm/MG400_ROS)

1.git clone 
```
cd $HOME/catkin_ws/src &&
git clone https://github.com/Dobot-Arm/MG400_ROS.git &&
cd $HOME/catkin_ws
```
2. make
```
catkin_make
```
3.activate workspace
```
source $HOME/catkin_ws/devel/setup.bash
```
4. run demo
```
roslaunch mg400_description display.launch
```
![alt text](https://github.com/NMB-MIC/utils/blob/main/jetson/dobot/ros/demo.JPG)
5. controlling robot
```
roslaunch dobot bringup.launch robot_ip:=192.168.1.6
```
