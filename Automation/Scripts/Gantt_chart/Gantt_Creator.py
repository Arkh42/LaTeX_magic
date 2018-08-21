"""
\file   Gantt_Creator.py
\brief  Python script which reads CSV files and generates LaTeX code to create Gantt charts.
"""


# --begin
print( "> Python script started: ongoing..." )


# Imports
import pgfgantt_csv2latex_writer

from tkinter import Tk
from tkinter.filedialog import askopenfilename


# Preventing the root window from appearing
main_window = Tk().withdraw()


# Asking for the *.csv file to open
input_file_name = str( askopenfilename() )
print( "> > File selected: " + input_file_name )

output_file_name = input_file_name.rpartition( "/" )[2] # Recovering the end of the file path, which is the file name.
output_file_name = output_file_name.partition( "." )[0] # Removing the file extension (e.g., ".csv").
output_file_name += ".tex"
print("> > File generated: " + output_file_name)


# Opening the files
with open( input_file_name, "r" ) as input_file :
    with open( output_file_name, "w" ) as output_file :

        gantt_writer = pgfgantt_csv2latex_writer.GanttWriter()
        
        # LaTeX code
        output_file.write( gantt_writer.open_gantt_environment( "2017-03-15", "2018-12-31" ) )
        output_file.write( gantt_writer.write_calendar_header() )

        print("> > Parsing the *.csv file: ongoing...")
        for line in input_file :
            output_file.write( gantt_writer.process_line( line ) )
        print("> > Parsing the *.csv file: done.")

        output_file.write( gantt_writer.close_gantt_environment() )


# --end
print( "> Python script successfully terminated." )