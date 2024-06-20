import openpyxl
import datetime

wb = openpyxl.Workbook()
wb.save("C:\\Programming\\Attendance\\Attendance.xlsx") 
wb.close()

# Load source and destination workbooks
wb_source = openpyxl.load_workbook('C:\\Programming\\Attendance\\Datasheet.xlsx')
wb_attendance = openpyxl.load_workbook('C:\\Programming\\Attendance\\Attendance.xlsx')
wb_attendance.create_sheet(index=0,title='Data')

# Get source sheet and create new sheet with today's date
source_sheet = wb_source['Data']
today = datetime.date.today().strftime("%d-%m-%y")
new_sheet = wb_attendance.create_sheet(today)

# Capture total names and details (assuming data starts from row 1)
total_names = source_sheet.max_column
total_details = source_sheet.max_row

# Copy names to new sheet (first column)
for row in range(1, total_details + 1):
    source_cell = source_sheet.cell(row=row, column=1)
    dest_cell = new_sheet.cell(row=row, column=1)
    dest_cell.value = source_cell.value

# Copy entire sheet to first sheet in attendance workbook
for row in range(1, total_details + 1):
    for col in range(1, total_names + 1):
        source_cell = source_sheet.cell(row=row, column=col)
        dest_cell = wb_attendance['Data'].cell(row=row, column=col)
        dest_cell.value = source_cell.value
        # Consider copying formatting and conditional formatting if needed

# Save the attendance workbook
wb_attendance.save('C:\\Programming\\Attendance\\Attendance.xlsx')
