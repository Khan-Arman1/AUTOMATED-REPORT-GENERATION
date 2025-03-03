# importing required modules
import pandas as pd     # for reading files
from fpdf import FPDF   # for creating pdfs

# creating a class, helps in writing in pdf file
class PDF(FPDF):
    # creates a header class method, adds header to all the pages
    def header(self):
        # set font takes
        self.set_font('Arial',"BU",18)
        # create cell
        self.cell(0,10,'Data Analysis Report',align='C')
        # line break
        self.ln()
    
    # add a heading before the content
    def heading(self,head_ing):
        # set font
        self.set_font('Times','BU',14)
        # set color
        self.set_text_color(0,0,0)
        # add heading
        self.cell(0,10,head_ing,align='L',ln=1)
    
    # table pdf normal text content takes 2 arguments text data and border value 0 or 1
    def content(self,data,b=0):
        # set font
        self.set_font('Times','',12)
        # set color
        self.set_text_color(0,0,0)
        # set cell
        self.multi_cell(0,10,data,ln=1,border=b)

    # create a hyerlink, takes 2 parametes link name and link address
    def hyperlink(self,name,link):
        # set font
        self.set_font('Times','',12)
        # set color
        self.set_text_color(0,0,255)
        # set cell
        self.cell(0,10,name,link=link,ln=1)

    # adding footer to all pages
    def footer(self):
        # set position of the footer
        self.set_y(-15)
        # set color
        self.set_text_color(0,0,0)
        # add font
        self.set_font('Courier','I',8)
        # add cell
        self.cell(0,10,f"Page {self.page_no()}/{{nb}}",align="C",ln=1)


# READING OF THE DATA SOURCE FILE
# specify the path
df=pd.read_csv('data.csv')

# CREATING A REPORT FILE
# initiallizing the pdf object
pdf = PDF('P','mm','A4')

# adding pages 
pdf.add_page()
# add metadata
pdf.set_author('Arman Khan')
pdf.set_title('Data Analysis Report')
pdf.set_subject('Data Analysis')
# get total no of page
pdf.alias_nb_pages()
# set auto page break
pdf.set_auto_page_break(auto=True,margin=10)

# create a brief intro
pdf.heading('# For this report:')
# add description of the pdf
pdf.content('I am using a CSV(Comma Separated File) file for data analysis. This file is available on W3schools pandas. This data analysis describes and provide information of the data. What type of value are in there, how many null values are present, does this dataframe have unique values, etc.')

# add dataframe
pdf.heading('# CSV DataFrame Overview:')
# add dataframe, set text color, set font
pdf.content('This is the dataframe that I have used in this file. Here, 1\'st column is the index, 2\'nd is Duration, 3\'rd is Pulse. 4\'th Maxpulse, 5\' is Calories.')
pdf.set_text_color(0,0,0)
pdf.set_font('Times','',12)
pdf.multi_cell(0,10,str(df),ln=1,align='C',border=1)
# create a hyper link to the website of where i found dataset
pdf.hyperlink('You can see the complete dataframe here, Dataframe','https://www.w3schools.com/python/pandas/data.csv.txt')
pdf.content('')
# create new page break
pdf.add_page()
# creating a description 
pdf.heading('# Descriptive Analysis Data:')
pdf.content('This is the description of dataframe. Here, 1\'st column is descriptive fields, 2\'nd is Duration, 3\'rd is Pulse. 4\'th Maxpulse, 5\' is Calories.')
# add dataframe, set text color, set font
pdf.set_text_color(0,0,0)
pdf.set_font('Times','',12)
pdf.multi_cell(0,10,df.describe().to_string(),ln=1,align="C",border=1)

# adding details, add details about what exactly is this data
pdf.set_font('Times','B',12)
pdf.cell(0,15,'* Lets breakdown:',ln=1)
pdf.content('\'COUNT\' - Number of all the values present i.e, 169,164')
pdf.content('\'MEAN\' - Mean value of the of that column values')
pdf.content('\'STD\' - Standard deviation value of the of that column values')
pdf.content('\'MIN\' - Min value of the of that column values')
pdf.content('\'25%\' - 25% of the Quartile range of that column values')
pdf.content('\'50%\' - 50% of the Quartile range of that column values')
pdf.content('\'75%\' - 75% of the Quartile range of that column values')
pdf.content('\'MAX\' - Max value of that column values')

# adding a note
pdf.set_font('Times','B',12)
pdf.cell(15,10,'Note:')
pdf.content("Quartile Range is method that help to find Outliers in the dataset, that are used in ML for prediction models.",b=1)

# add a new page break
pdf.add_page()
# adding info of the data, set text color, set font
pdf.heading('# Informational Analysis Data')
pdf.content('Information of values present in the dataframe. Like - values count, unique values, null values, etc.')
pdf.set_font('Times','B',12)
pdf.cell(0,12,'* Null value analysis',ln=1)
# adding null value count, count for how many null values present
pdf.content(f'Check Null Values in column and return sum  : Total null values present')
pdf.content(f'Null Values in \'Duration\' : {str(df['Duration'].isnull().sum())} values present.')
pdf.content(f'Null Values in \'Pulse\' : {str(df['Pulse'].isnull().sum())} values present.')
pdf.content(f'Null Values in \'Maxpulse\' : {str(df['Maxpulse'].isnull().sum())} values present.')
pdf.content(f'Null Values in \'Calories\' : {str(df['Calories'].isnull().sum())} values present.')
# adding a note
pdf.set_font('Times','B',12)
pdf.cell(15,10,'Note:')
pdf.content("Here, In \'Calories\' sum is 5 stats total 5 null values are present in this column and 0 means no null value.",b=1)


# uniqure values
pdf.set_font('Times','B',12)
pdf.cell(0,12,'* Unique values present',ln=1)
# adding unique value 
pdf.content(f'Values count in column and return sum  : Total of no. of values')
pdf.content(f'Values count in \'Duration\' : {str(df['Duration'].unique().sum())} sum of unique values present.')
pdf.content(f'Values count in \'Pulse\' : {str(df['Pulse'].unique().sum())} sum of unique values present.')
pdf.content(f'Values count in \'Maxpulse\' : {str(df['Maxpulse'].unique().sum())} sum of unique values present.')
pdf.content(f'Values count in \'Calories\' : {str(df['Calories'].unique().sum())} sum of unique values present.')
# adding a note
pdf.set_font('Times','B',12)
pdf.cell(15,10,'Note:')
pdf.content("This data is provided on the basis of how many unique values are present and the sum of all the values.",b=1)


# value counts, count for how many values are present
pdf.set_font('Times','B',12)
pdf.cell(0,12,'* Values Counts in the field',ln=1)
# adding value count data
pdf.content(f'Unique records in column  : Total of no. of values')
pdf.content(f'Unique records in \'Duration\' : {str(df['Duration'].value_counts().sum())} sum of values present.')
pdf.content(f'Unique records in \'Pulse\' : {str(df['Pulse'].value_counts().sum())} sum of values present.')
pdf.content(f'Unique records in \'Maxpulse\' : {str(df['Maxpulse'].value_counts().sum())} sum of values present.')
pdf.content(f'Unique records in \'Calories\' : {str(df['Calories'].value_counts().sum())} sum of values present.')
# adding a note
pdf.set_font('Times','B',12)
pdf.cell(15,10,'Note:')
pdf.content("There are total count of record is 169 and in 'Calories' count if 164, means it consists null values.",b=1)

# add break
pdf.add_page()
# dtype of the value
pdf.set_font('Times','B',12)
pdf.cell(0,12,'* DataType of the values',ln=1)
# adding datatype
pdf.content('Values in dataframe  : Type of values')
pdf.content(f'Datatype of values in \'Duration\'  :  \'{str(df['Duration'].dtype)}\' type.')
pdf.content(f'Datatype of values in \'Pulse\'  :  \'{str(df['Pulse'].dtype)}\' type.')
pdf.content(f'Datatype of values in \'Maxpulse\'  :  \'{str(df['Maxpulse'].dtype)}\' type.')
pdf.content(f'Datatype of values in \'Calories\'  :  \'{str(df['Calories'].dtype)}\' type.')
# adding a note
pdf.set_font('Times','B',12)
pdf.cell(15,10,'Note:')
pdf.content("int64 stats Integer value, float64 stats Floating Point values, and object32 stats String/object value.",b=1)


# output of the file
pdf.output('pdf_1.pdf')

# in the above code only states details of the data present in the file, this data is not cleaned