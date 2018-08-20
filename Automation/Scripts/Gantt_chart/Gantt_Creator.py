"""
\file   Gantt_Creator.py
\brief  Python script which reads CSV files and generates LaTeX code to create Gantt charts.
"""


# --begin
print( "> Python script started: ongoing..." )


# Imports
import pgfgantt_csv2latex_writer


# Opening the files
input_file_name = "PhD_thesis_planning.csv"
output_file_name = "PhD_thesis_planning.tex"

with open( input_file_name, "r" ) as input_file :
    with open( output_file_name, "w" ) as output_file :

        gantt_writer = pgfgantt_csv2latex_writer.GanttWriter()
        
        # LaTeX code
        output_file.write( gantt_writer.open_gantt_environment( "2017-03-15", "2018-12-31" ) )
        output_file.write( gantt_writer.write_calendar_header() )

        for line in input_file :
            output_file.write( gantt_writer.process_line( line ) )

        output_file.write( gantt_writer.close_gantt_environment() )


# --end
print( "> Python script successfully terminated." )