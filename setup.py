from distutils.core import setup
import os
import subprocess

"""
if os.path.exists("debian/changelog"):
    output=subprocess.check_output("parsechangelog | grep Version", shell=True)
    version = output.split(":")[1].strip()
"""

setup(name = "ros-system-workstation",
    #version = version,
    version = "0.0.1",
    description = "ROS Workstation",
    author = "I Heart Engineering",
    author_email = "code@iheartengineering.com",
    url = "http://www.iheartengineering.com",
    license = "BSD-3-clause",
    scripts = ["dynamic-reconfigure", "rviz", "rxconsole", "rxloggerlevel"],
    data_files=[('/usr/share/applications', ["ros-dynamic-reconfigure.desktop"]),
                ('/usr/share/applications', ["ros-gazebo.desktop"]),
                ('/usr/share/applications', ["ros-group.desktop"]),
                ('/usr/share/applications', ["ros-network-id.desktop"]),
                ('/usr/share/applications', ["ros-roscore.desktop"]),
                ('/usr/share/applications', ["ros-roslaunch.desktop"]),
                ('/usr/share/applications', ["ros-rviz.desktop"]),
                ('/usr/share/applications', ["ros-rxbag.desktop"]),
                ('/usr/share/applications', ["ros-rxconsole.desktop"]),
                ('/usr/share/applications', ["ros-rxgraph.desktop"]),
                ('/usr/share/applications', ["ros-rxloggerlevel.desktop"]),
                ('/usr/share/mime-info', ["ros-roslaunch.mime"]),
                ('/usr/share/mime/packages', ["ros-roslaunch.xml"]),
                ('/usr/share/desktop-directories', ["Robotics.directory"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/application-x-ros-launch.svg"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/ros-rviz.svg"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/ros-rx.svg"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/ros-tool.svg"]),
               ],
    long_description = """ROS Workstation Environment""" 
    #classifiers = []     
) 
