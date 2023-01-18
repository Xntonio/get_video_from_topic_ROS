# get_video_from_topic_ROS
This script uses OpenCV to read and save a monochrome video from and to a topic in ROS in MP4 format, without having to rely on cv_bridge.

This script is responsible for reading a monochrome video from a topic in ROS and saving it in MP4 format. It uses the OpenCV library for reading and writing video data, instead of ROS's built-in video handling functions.

1.The script subscribes to the specified monochrome video topic.
2.Uses OpenCV functions to read video data from the topic.
3.Creates an MP4 video file in the specified path.
4.Uses OpenCV functions to write the video data to the MP4 file.
5.The script runs continuously until manually stopped or until the end of the video is reached.
6.The saved video can be played back with any MP4 compatible video player.

This script is useful for storing monochrome videos in a standard format for further processing or analysis, without having to rely on cv_bridge.
