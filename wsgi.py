"""Application entry point."""
from flask_wtforms_tutorial import create_app
from flask import Flask, render_template
from flask import Flask, redirect
from flask import Flask, make_response


app = Flask(
    __name__,
    template_folder="templates"
)

@app.route("/")
def home():
    """Serve homepage template."""
    return render_template(
        'index.html',
        title='Flask-Login Tutorial.',
        body="You are now logged in!"
    )

@app.errorhandler(404)
def not_found():
    """Page not found."""
    return make_response(
        render_template("404.html"),
        404
     )


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(
        render_template("400.html"),
        400
    )


@app.errorhandler(500)
def server_error():
    """Internal server error."""
    return make_response(
        render_template("500.html"),
        500
    )

app = create_app()
app.config['SECRET_KEY'] = 'any secret string'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)