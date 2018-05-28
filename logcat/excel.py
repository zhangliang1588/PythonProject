#! -*-coding:utf-8-*-

import xlwt
from xlwt import XFStyle,Font,Alignment,easyxf

class Excel():
    """将数据写入到excel表的类"""
    def __init__(self):
        self.title_style = easyxf("font:bold on;align:wrap on ,vert centre,horz center")
        self.cell_style = easyxf("align:wrap on,vert centre,horz center")
        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet_name1 = '拍照响应时间'
        
    def init_sheet(self,sheet):
        sheet.col(0).width = 256*15
        sheet.col(1).width = 256*10
        sheet.col(2).width = 256*10
        sheet.col(3).width = 256*10
        sheet.col(4).width = 256*10
        sheet.col(5).width = 256*10
        sheet.col(6).width = 256*10
        sheet.col(7).width = 256*10
        sheet.col(8).width = 256*10
        sheet.col(9).width = 256*10
        sheet.col(10).width = 256*10
        sheet.col(11).width = 256*10
        
        sheet.write(0,0,'次数',self.title_style)
        sheet.write(0,1,'第一次',self.title_style)
        sheet.write(0,2,'第二次',self.title_style)
        sheet.write(0,3,'第三次',self.title_style)
        sheet.write(0,4,'第四次',self.title_style)
        sheet.write(0,5,'第五次',self.title_style)
        sheet.write(0,6,'第六次',self.title_style)
        sheet.write(0,7,'第七次',self.title_style)
        sheet.write(0,8,'第八次',self.title_style)
        sheet.write(0,9,'第九次',self.title_style)
        sheet.write(0,10,'第十次',self.title_style)
        sheet.write(0,11,'平均值',self.title_style)
        sheet.write(1,0,'拍照时间',self.title_style)
        
    def init_sheet1(self):
        self.sheet1 = self.workBook.add_sheet(self.sheet_name1)
        self.init_sheet(self.sheet1)
    
    
    def fill_to_cell(self,sheet,content,row,col):
        sheet.write(row,col,content,self.cell_style)
        
      
    def fill_to_sheet(self,sheet,capture_totalTimes,average_time):
        current_row = 1
        current_col = 1
        for capture_time in capture_totalTimes:
            self.fill_to_cell(sheet,capture_time,current_row,current_col)
            current_col += 1    
        self.fill_to_cell(sheet,average_time,current_row,current_col)
    
    def fill_to_sheet1(self,capture_totalTimes,average_time):
        self.fill_to_sheet(self.sheet1,capture_totalTimes,average_time)
    
    def save_workbook(self):
        self.workBook.save('性能测试结果.xls')
        
        