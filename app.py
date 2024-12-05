from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    # define our list of dictionaries where each dictionary represents a project (Image, Title, and Description)
    projects = [{"image": "/static/images/project_1_img.webp",
                 "title": "PERL PROGRAMMING",
                 "description": "Created an HTML customer registration pform where you ask the Name, address, phone number, email address and photograph and displays it in a nice format.",
                 "github": "https://www2.scs.ryerson.ca/~m27mirza/cgi-bin/lab07b.html"},
                {"image": "/static/images/project_2_img.webp",
                 "title": "PHP PROGRAMMING",
                 "description": "Created a form that asks the visitor for two integer numbers. A multiplication table will be generated using those 2 integer numbers. ",
                 "github": "https://www.cs.ryerson.ca/~m27mirza/lab08/page2.php"}]

    return render_template('index.html', projects=projects)


@app.route('/reflection')
def reflection():
    return render_template('reflection.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
