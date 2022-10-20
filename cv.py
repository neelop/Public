# Text Variables
Name = 'PIOTR WRZASZCZ'
Title = 'Junior Python Developer'
Contact = 'Gdansk, PL\n' \
          '606-965-347\n' \
          'pwrzaszcz@gmail.com\n' \
          'github.com/neelop'

WorkHeader = 'EXPERIENCE'
WorkOneTitle = 'Twoj Doradca - Accounting Office / System Administrator'
WorkOneTime = '02/2020-Present'
WorkOneDesc = '- Maintain essential IT operations, including operating systems, security tools,\n' \
              ' applications, servers, email systems, laptops, desktops, software, and hardware\n' \
              '- Management and maintenance of database archive\n' \
              '- Nurture dependable IT infrastructure and networking\n' \
              '- Monitoring system performance and troubleshooting issues\n' \
              '- Scripting to improve workflow'

WorkTwoTitle = 'Staples Solutions / Margin Analyst'
WorkTwoTime = '2/2019-12/2019'
WorkTwoDesc = '- Introduces the data-driven approach to realizing pricing strategy \n' \
              'for emerging B2C channels\n' \
              '- Using statistical models to push relevant pricing and strategies \n' \
              'and drive sales/margin gains\n' \
              '- Identifying opportunities to improve existing pricing and margin\n' \
              'models and support the development team in building new ones\n' \
              'Initiating support development and implementing structural\n' \
              'analytical techniques and ideas\n' \
              'Supporting markets in activities, analysis, and reporting that will\n' \
              'result in effective margin management\n' \
              'task and assignment distribution in EMEA region'
EduHeader = 'EDUCATION'
EduOneTitle = 'Gdansk University of Technology,\n' \
              'B.S. Mechanical Engineering and \n' \
              'Machine Design, \n2011-2014'
EduTwoTitle = 'Gdansk University of Technology,\n' \
              'B.S. Applied Mathematics, \n2016-current'
EduTwoTime = '2016-current'
SkillsHeader = 'Skills'
SkillsDesc = '- Python\n- Django\n- SQL\n- Linux\n- Docker\n- C++\n- Git\n- English'
ExtrasTitle = 'DataQuest\nData Scientist Path'
ExtrasDesc = 'Learned popular data science\nlanguages, data cleaning and\nmanipulation, machine learning \nand statistical analysis'
CodeTitle = 'View Portfolio'

# Setting style for bar graphs
import matplotlib.pyplot as plt


# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text
plt.annotate(Name, (.02,.94), weight='bold', fontsize=20)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=14)
plt.annotate(Contact, (.7,.906), weight='regular', fontsize=8, color='#ffffff')
plt.annotate(WorkHeader, (.02,.86), weight='bold', fontsize=10, color='#58C1B2')
plt.annotate(WorkOneTitle, (.02,.832), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.81), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04,.71), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.68), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.662), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.485), weight='regular', fontsize=9)
plt.annotate(SkillsHeader, (.7,.8), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.65), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(EduHeader, (.7,.6), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(EduOneTitle, (.7,.535), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(EduTwoTitle, (.7,.48), weight='regular', fontsize=10, color='#ffffff')

#plt.show()
plt.savefig('resumeexample.png', dpi=300, bbox_inches='tight')