from flask import Flask

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)


@app.route('/')
def mainPage():
  return "Hello World"

if __name__ == "__main__":  # is dit bestand main proces
  app.run(  # Starts the site
      debug=True, # Restarts on code-change
      host='0.0.0.0' # Listen on 0.0.0.0
  )
