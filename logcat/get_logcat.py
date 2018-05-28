#!-*-coding:utf-8-*-

import os
import datetime
import time
from excel import Excel

class AppPerformance():
    """测试相机APP性能的类"""
    def __init__(self):
        self.excel = Excel()
        

    def get_logcat_file(self):
        cmd_getLogcatFile = 'adb pull /cache/logs/logcat/logcat_main.txt '
        os.popen(cmd_getLogcatFile)
        time.sleep(5)

    
    def run_autotest(self):
        cmd_start_camera = 'adb shell am start -W com.zte.camera'
        cmd_capture = 'adb shell input keyevent 27'
        cmd_stop_camera = 'adb shell am force-stop com.zte.camera'
        os.popen(cmd_start_camera)
        for index in range(10):
            os.popen(cmd_capture)
        
        os.popen(cmd_stop_camera)
    
    
    def get_logcat_keyLines(self):
        thumbnail_numbers = 0
        self.captureLog_lines = []
        self.thumbnailsLog_lines = []
        self.testappLog_lines = []
        
        with open('logcat_main.txt','r',encoding='gbk',errors='ignore') as read_file:
            while True:
                buffer = read_file.readline()
                if not buffer:
                    break
                elif 'ThumbnailView' in buffer:
                    thumbnail_numbers += 1
                    if thumbnail_numbers != 1:
                        self.thumbnailsLog_lines.append(buffer)
                elif 'ZTE_CAM_ShutterButton' in buffer:
                    self.captureLog_lines.append(buffer)
                elif 'Test APP Starts To Capture' in buffer:
                    self.testappLog_lines.append(buffer)
        
        
    def get_formatted_time(self):
        self.capture_times = []
        self.thumbnail_times = []
        self.testapp_times = []
        for captureLog_line in self.captureLog_lines:
            temp_time = datetime.datetime.strptime(
                captureLog_line.split(' ')[1],'%H:%M:%S.%f')
            self.capture_times.append(temp_time)
    
        for thumbnailLog_line in self.thumbnailsLog_lines:
            temp_time = datetime.datetime.strptime(
                thumbnailLog_line.split(' ')[1],'%H:%M:%S.%f')
            self.thumbnail_times.append(temp_time)    
    
        for testappLog_line in self.testappLog_lines:
            temp_time = datetime.datetime.strptime(
                testappLog_line.split(' ')[1],'%H:%M:%S.%f')
            self.testapp_times.append(temp_time)  
    
    
    def get_capture_totalTime(self):
        self.capture_totalTimes = []
        for index in range(len(self.capture_times)):
            capture_responseTimeSub = self.capture_times[index].__sub__(
                self.testapp_times[index])
            thumbnail_generateTimeSub = self.thumbnail_times[index].__sub__(
                self.capture_times[index])
            capture_responseTime = capture_responseTimeSub.seconds + \
                capture_responseTimeSub.microseconds/1e6
            thumbnail_generateTime = thumbnail_generateTimeSub.seconds + \
                thumbnail_generateTimeSub.microseconds/1e6
            capture_Totaltime = capture_responseTime + thumbnail_generateTime
            self.capture_totalTimes.append(float(format(capture_Totaltime,'0.3f')))
        
        self.average_time = sum(self.capture_totalTimes)/len(self.capture_totalTimes)
    
    def fill_to_excel(self):
        self.excel.init_sheet1()
        self.excel.fill_to_sheet1(self.capture_totalTimes,self.average_time)
        self.excel.save_workbook()
    
def run():
    appPerformance = AppPerformance()
    appPerformance.get_logcat_file()
    appPerformance.get_logcat_keyLines()
    appPerformance.get_formatted_time()
    appPerformance.get_capture_totalTime()
    appPerformance.fill_to_excel()
    
    
if __name__ == '__main__':
    run()
            
        
    
                