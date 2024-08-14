import os
import subprocess
import sys
import tkinter as tk
from tkinter import filedialog

def select_directory(title):
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title=title)
    return directory

def extract_frames(input_dir, output_dir):
    # 確保主輸出目錄存在
    os.makedirs(output_dir, exist_ok=True)

    # 指定 ffmpeg 的完整路徑
    ffmpeg_path = r"C:\FFmpeg\ffmpeg-2024-08-11-git-43cde54fc1-full_build\bin\ffmpeg.exe"  # 請將此路徑替換為您系統中 ffmpeg.exe 的實際路徑

    # 遍歷輸入目錄中的所有MP4文件
    for filename in os.listdir(input_dir):
        if filename.endswith('.mp4'):
            name_without_ext = os.path.splitext(filename)[0]
            
            video_output_dir = os.path.join(output_dir, name_without_ext)
            os.makedirs(video_output_dir, exist_ok=True)
            
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(video_output_dir, f'{name_without_ext}_%d.png')
            
            command = [
                ffmpeg_path,  # 使用指定的 ffmpeg 路徑
                '-i', input_path,
                '-vf', 'fps=1',
                output_path
            ]
            
            try:
                subprocess.run(command, check=True, stderr=subprocess.PIPE, text=True, encoding='utf-8')
                print(f"完成處理視頻: {filename}")
            except subprocess.CalledProcessError as e:
                print(f"處理視頻 {filename} 時出錯:")
                print(e.stderr)

    print("所有視頻的幀提取完成。")

if __name__ == "__main__":
    print("請選擇輸入視頻所在的目錄")
    input_dir = select_directory("選擇輸入目錄")
    
    print("請選擇輸出幀的目錄")
    output_dir = select_directory("選擇輸出目錄")
    
    if input_dir and output_dir:
        extract_frames(input_dir, output_dir)
    else:
        print("未選擇目錄，程序結束。")
    
    input("按Enter鍵結束程序...")
