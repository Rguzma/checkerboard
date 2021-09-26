from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')
def index():
    return render_template("index.html",td1=8, td2=8, color_one="red",color_two="black")


@app.route('/<int:num>/<int:num2>')
def numberChange(num, num2):
    return render_template("index.html",td1=num, td2=num2, color_one="red",color_two="black")

@app.route('/<int:num>/<int:num2>/<string:colora>')
def colorchange(num, num2, colora):
    return render_template("index.html",td1=num, td2=num2, color_one=colora, color_two="black")


@app.route('/<int:num>/<int:num2>/<string:colora>/<string:colorb>')
def doublecolorchange(num, num2, colora, colorb):
    return render_template("index.html",td1=num, td2=num2, color_one=colora, color_two=colorb)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    # app.run(debug=True) should be the very last statemen