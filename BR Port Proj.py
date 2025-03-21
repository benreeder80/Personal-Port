import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Ben Reeder - Sr. Data Analyst
##### *Data-Driven Strategist | Optimization & Analytics Specialist* 
''')

image = Image.open('IMG_0984.png')
st.image(image, width=125,)
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Sr. Data Analyst with over 4 years of experience specializing in transforming complex datasets into actionable insights that drive strategic business decisions and optimize operations.
- Proficient in Python, SQL, Power BI, cloud computing, and AI with a strong focus on data storytelling and process automation.
- Recognized for leading high-impact projects, including generating over $1.6 million in revenue through A/B testing and saving hundreds of hours per month by streamlining data processes.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #D4EDDA;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/ben-reeder80/" target="_blank">Ben Reeder</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

    #####################
st.markdown('''
## Work Experience
''')

txt('**Senior Data Analyst** - PRA Group',
'Nov. 2023-Present')
st.markdown('''
- Designed and implemented a Legal Scorecard using SQL, Power BI, and Python while ensuring data quality and enabling performance testing in compliance with State-level regulatory standards.
- Scorecard is shared with external firms to foster competition and used internally to strategically place accounts in each State through automation based on performance to maximize collections at each legal stage.
''')

txt('**Data Analyst** - PRA Group',
'Aug. 2022')
st.markdown('''
- Worked on Legal Strategy team focusing on optimizing expenditures and operations through automation and strategic decisions using SQL, Power BI, and Python.
- Developed and executed automated A/B testing frameworks, resulting in over $1.6 million in gross revenue and a 750% ROI, that not only optimized legal settlement strategies but also served as a model for future settlement letter testing. 
- Led project to improve data quality from external firms, enhancing analysis accuracy across all Data and Analytics departments through communication with Data Engineering team as well as individual firms. 
''')


txt('**Data Analyst** - Deloitte',
'Nov. 2021')
st.markdown('''
- Led a team project to develop a data model and database using SQL and Python for a project initiative, administering the database for executive-level reporting.
- Managed database schema changes and modernization, planning the transfer of applications to Microsoft Power Platform (Dataverse, Power Apps, Power Automate) to increase process efficiency.

''')

txt('**Data Analyst** - Stairway Limited',
'Mar. 2021')
st.markdown('''
- Discovered new methods of pulling parcel data for a multitude of zonings, cities, and states.
- Streamlined data cleansing/extraction processes utilizing web scraping/data cleaning in Python, Macros in Excel and SQL Server to eliminate tedious data cleaning tasks while saving on average 100 hours per month for the business.
- Increased efficiency by saving an average of $4,000 per month when data was sent through skip-tracing service.
''')

#####################
st.markdown('''
## Projects
''')
txt4('Proj 1 Name', 'Proj 1 Description', 'https://github.com/benreeder80')
txt4('Proj 2 Name', 'Proj 2 Description', 'https://github.com/benreeder80')
txt4('Proj 3 Name', 'Proj 3 Description', 'https://github.com/benreeder80')
txt4('Proj 4 Name', 'Proj 4 Description', 'https://github.com/benreeder80')
txt4('Proj 5 Name', 'Proj 5 Description', 'https://github.com/benreeder80')


st.markdown ('''
## Upwork Proposal Automation
''')

# Your Loom video ID
video_id = "c69a3fdcbe7c4ed7973fc2beebe3bc9e"

# Loom Embed iframe
embed_code = f"""
<iframe src="https://www.loom.com/embed/{video_id}" 
        frameborder="0" 
        webkitallowfullscreen 
        mozallowfullscreen 
        allowfullscreen 
        width="700" 
        height="400">
</iframe>
"""

# Display in Streamlit
st.markdown(embed_code, unsafe_allow_html=True)


#st.title("Embedded Power BI Report in Streamlit")

# Your Power BI report URL
#power_bi_report_url = "https://app.powerbi.com/view?r=8a494028-b171-4480-b2bd-55b594bfc162"

# Embed Power BI in an iframe
#embed_code = f"""
#<iframe title="Power BI Report"
 #       width="900" height="600"
  #      src="{power_bi_report_url}"
   #     frameborder="0" 
    #    allowFullScreen="true">
#</iframe>
#"""

# Display in Streamlit
#st.markdown(embed_code, unsafe_allow_html=True)



#####################
st.markdown('''
## Skills
''')

txt3('Data Processing', '`Python`,`SQL`, `Pandas`, `Numpy`')
txt3('Data Visualization', '`Power BI`, `Tableau`, `Matplotlib`, `Seaborn`, `Plotly`')
txt3('AI Agents/Automation', '`Prompt Engineering`, `N8N`, `Make.com`')
txt3('Cloud', '`Azure`')

#####################
st.markdown('''
## Certifications
''')

txt('**AZ-900** - Microsoft Certified Data Analyst Associate',
'Mar. 2025')
st.markdown('''
- Demonstrated foundational knowledge of cloud concepts, Azure services, security, compliance, and cost management.

''')

txt('**DA-100/PL-300** - Microsoft Certified Data Analyst Associate',
'Jan. 2022')
st.markdown('''
- Exhibited expertise of all components within Power BI for Data Analytics such as the DAX/M languages, Data Modeling/Cleaning in Power Query, and Visualizations/Dashboards.

''')

txt('**Google Data Analytics Professional Certificate**',
'Jun. 2021')
st.markdown('''
- Studied Microsoft Excel, Tableau, SQL (BigQuery), and R to wrangle, clean, manipulate, and visualize large sets of data along with understanding how these tools solve real-world business problems.

''')



#####################
st.markdown('''
## Education
''')



txt('**Bachelors of Science** (Business Data Analytics),  *Arizona State University*',
'2020-2022')
st.markdown('''
- GPA: `3.91`
- Graduated Summa Cum Laude
- Coursework included Big Data for Business Analytics, Enterprise Analytics, Business Data Mining, Python Programming for Business Analytics, and Data Warehousing/Modeling while interacting with a number of tools such as AWS, Spark/PySpark, Python, Excel, SQL (SQL Server), Tableau and various statistical software such as IBM SPSS and JMP.
''')
















#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/ben-reeder80/')
txt2('GitHub', 'https://github.com/benreeder80')

