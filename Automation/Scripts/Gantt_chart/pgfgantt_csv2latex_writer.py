class GanttWriter :
    """Class intended for writing LaTeX files to generate Gantt charts from csv files as  user interface.
    It is characterised by
    - 
    """


    def __init__( self ) :
       self.fields = list()


    # Opening and closing the LaTeX environment
    def open_gantt_environment( self, start, end ) :
        return "\\begin{ganttchart}[%\n\tvgrid,%\n\ttime slot format=isodate,%\n\ttime slot unit=month,%\n]{" + start + "}{" + end + "}\n"

    def close_gantt_environment( self ) :
        return "\\end{ganttchart}"
    

    # Writing specific piece of information in the Gantt chart
    def write_calendar_header( self ) :
        return "\t\\gantttitlecalendar{year, month} \\\\ \n"
    
    def write_gantt_workpackage( self, workpackage, start, end ) :
        return "\t%\n\t\\ganttgroup{" + workpackage + "}{" + start + "}{" + end + "} \\\\ \n"

    def write_gantt_task( self, label, task, start, end ) :
        return "\t\\ganttbar[name=" + label + "]{" + task + "}{" + start + "}{" + end + "} \\\\ \n"
    
    def write_gantt_milestone( self, label, milestone, date ) :
        return "\t\\ganttmilestone[name=" + label + "]{" + milestone + "}{" + date + "}\\\\ \n"
    
    def write_gantt_link( self, first_element, second_element ) :
        return "\t\\ganttlink{" + first_element + "}{" + second_element + "} \n"


    # Automatic processing
    def process_line( self, textline ) :

        # Check if textline is empty
        if textline.strip() == "" :
            print( "> > Empty line... ignored.")
            return ""

        # Split on comma and remove extra white space
        self.fields = [ field.strip() for field in textline.split( sep = "," ) ]

        # Parsing
        symbol = self.fields[0]
        label = self.fields[1]

        if symbol == "#" :
            print( "> > Comment detected ('#' symbol)... ignored." )
            return ""
        elif symbol == "W" :
            print( "> > Workpackage being written." )
            return self.write_gantt_workpackage( self.fields[2], self.fields[3], self.fields[4] )
        elif symbol == "T" :
            print( "> > Task being written." )
            return self.write_gantt_task( label, self.fields[2], self.fields[3], self.fields[4] )
        elif symbol == "M" :
            print( "> > Milestone being written.")
            return self.write_gantt_milestone( label, self.fields[2], self.fields[3] )
        elif symbol == 'L' :
            print( "> > Link being written." )
            return self.write_gantt_link( self.fields[1], self.fields[2] )
        else :
            print( "> > Unknown key. Please check the csv file.")
            return ""