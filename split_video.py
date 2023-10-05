import subprocess

# Input video file
input_video = "input_video.mkv"

# Define timecodes and project names
timecodes = [
    ("00:07:01", "00:30:25", "Color_Flipper"),
    ("07:01:30", "07:44:04", "Counter"),
    ("30:25:44", "1:11:29", "Reviews"),
    ("00:44:04", "01:11:29", "Navbar"),
    ("01:11:29", "01:26:21", "Sidebar"),
    ("01:26:21", "01:39:03", "Modal"),
    ("01:39:03", "01:48:26", "Questions"),
    ("01:48:26", "02:16:25", "Menu"),
    ("02:16:25", "03:16:13", "Video"),
    ("03:16:13", "03:32:45", "Scroll"),
    ("03:32:45", "04:36:15", "Tabs"),
    ("04:36:15", "04:58:53", "Countdown"),
    ("04:58:53", "05:56:35", "Lorem_Ipsum"),
    ("05:56:35", "06:18:23", "Grocery"),
    ("06:18:23","08:01:14", "Slider")
]

# Loop through timecodes and generate FFmpeg commands
for start_time, end_time, project_name in timecodes:
    output_file = f"{project_name}.mkv"
    cmd = [
        "ffmpeg",
        "-ss", start_time,
        "-t", end_time,
        "-i", input_video,
        "-c:v", "copy",
        "-c:a", "copy",
        output_file
    ]

    # Execute the FFmpeg command
    subprocess.run(cmd)

print("All projects extracted.")
