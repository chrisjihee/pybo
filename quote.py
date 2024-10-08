from random import choice

from flask import Flask, redirect, url_for
from flask_classful import FlaskView, route

# we'll make a list to hold some quotes for our app
quotes = [
    "A noble spirit embiggens the smallest man! ~ Jebediah Springfield",
    "If there is a way to do it better... find it. ~ Thomas Edison",
    "No one knows what he can do till he tries. ~ Publilius Syrus"
]

server = Flask(__name__)


class QuotesView(FlaskView):
    def index(self):
        return "<br>".join(quotes)

    def get(self, id):
        id = int(id)
        if id < len(quotes):
            return quotes[id]
        else:
            return "Not Found", 404

    @route('/random', endpoint='ran')
    def random(self):
        return choice(quotes)

    def move(self):
        return redirect(url_for('QuotesView:index'))

    def move2(self):
        return redirect(url_for('ran'))


QuotesView.register(server)


@server.route("/")
def home():
    return redirect(url_for('QuotesView:index'))


if __name__ == '__main__':
    server.run()
