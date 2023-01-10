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
      debug=True,
      host='0.0.0.0'  # req. for repl
  )
