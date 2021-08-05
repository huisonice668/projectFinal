"""Application entry point."""
from flask_wtforms_tutorial import create_app
app = create_app()
app.config['SECRET_KEY'] = 'secret'

# Using a production configuration
app.config.from_object('config.ProdConfig')

# Using a development configuration
app.config.from_object('config.DevConfig')



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)