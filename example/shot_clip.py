import sys
import cv2
import os
import pathlib
import traceback

def video_to_clips(video_file, output_folder, resize=1):
    #os.makedirs(output_folder)
    video_cap = cv2.VideoCapture(str(video_file))
    fps = video_cap.get(cv2.CAP_PROP_FPS)
    vid_name = os.path.splitext(os.path.basename(str(video_file)))[0]
    clip_name = os.path.join(output_folder, '%s_clip_%%05d.mp4' % vid_name)
    #fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_length = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
    #print(video_length)

    init = True
    frames = []
    while video_cap.isOpened():
        # Get the next video frame
        res, frame = video_cap.read()
        if not res:
            break
        frames.append(frame)

    i = 0
    for shot_item in shot_frames:
        print(shot_item)
        clip_cap = cv2.VideoWriter(clip_name % i,fourcc,fps,(1280, 720))
        for frame in frames[shot_item[0]:shot_item[1]]:
            clip_cap.write(frame)
        i+=1

if __name__ == "__main__":
    #video_shot_file= "reult.log"
    #video_shot_frames = get_shot_frames(video_shot_file)
    #print(video_shot_frames)
    #sys.exit(1)
    shot_frames = []
    with open("./video/test.mp4.scenes.txt", "r") as fp:
        for line in fp:
            s_indexs = line.strip().split(" ")
            shot_frames.append((int(s_indexs[0]), int(s_indexs[1])))

    out_dir = "./out"
    input_dir = "./video/test.mp4"
    file_list  = pathlib.Path(input_dir)
    video_to_clips(file_list, out_dir)


