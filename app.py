from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<category>')
def retrieve_page(category):
    # TODO: validate whether real category

    # TODO: check database for locations corresponding to categories
    locations = [('thing1', 'thing2', 'thing3'), ('thing1', 'thing2', 'thing3')]

    return render_template('category_template.html', category=category,
                           locations=locations)


if __name__ == '__main__':
    app.run()
