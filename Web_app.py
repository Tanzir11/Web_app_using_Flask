#One good place to find dope images for our website is Unsplash.com here we get royalty free images
'''The html file we have created corresponding to this file have very interesting stuff. First of all in that file we have used
html as well as CSS. Right after title we had a style tag which suggests that we will be using 
CSS in that when we gave h1 tag and changed the font and colour of the file  and when we did that it effectively changed the fonts 
of every h1 header save with h2, para and button. We have also used text line centre and other stuff and in rgb section what we did was we added 
different parts of red with blue and green to make with different colours
<div style="text-align:center;"> We also used this line and what it does is that it places the button at the center where it was not previously'''
from flask import Flask, render_template

app=Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Bangluru, India',
        'Salary': 'Rs 10,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi, India',
        'Salary':'Rs 15,00,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'Remote'
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location':'San Francisco, USA',
        'Salary':'$120,000'
    }
]

@app.route("/")
def hey():
    return render_template('project1_basic_html_no_CSS.html', jobs=JOBS)

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)

'''There is one very interesting approach i took in file project1_alternative_approach and what was i first of all created a paragragh tag
and in that paragraph tag i defined a class on one of them and change the given attributes of that para like fonts, size and etc.
Now whenever i would define a new para the moment i would mention the class if it's same it will go back to it's previous attributes 
and if not it would get a new attributes as we can see the difference in the two project based html files. 
'''
'''
 there is the 3rd html same project file but with no CSS their we'd use what front end people have already done and use 
 that in an order to make our website look dope also keep that in mind that 
 it's called bootstraped frontend stuff,
 If you are looking for go to www.getbootstrap.com
 '''
'''
 one other this is that we created another html file and in our project1_basic_html_no_CSS.html folder we wrote these lines
 {% for job in jobs %}
            {% include 'jobitem.html' %}
            {% endfor %}
            and we created another folder called jobitem.html
and with this line {% include 'jobitem.html' %}
i have merged the jobitem folder at the perticular desired spot depending upon it's position and now jobitem thinng will render with it
'''
