#!/usr/bin/env python3

from flask import Flask, request, render_template_string

app = Flask(__name__)

STYLE = """
<style>
    body { font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }
    .container { max-width: 700px; margin: auto; background: white; padding: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
    h2 { text-align: center; color: #333; }
    form { margin-top: 30px; }
    input[type=text] { width: 70%; padding: 10px; margin: 10px 0; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
    input[type=submit] { width: 28%; background-color: #5cb85c; color: white; padding: 10px; border: none; border-radius: 4px; cursor: pointer; }
    input[type=submit]:hover { background-color: #45a049; }
</style>
"""

@app.route("/")
def main():
    return render_template_string(STYLE + '''
     <div class="container">
         <h2>Enter your text</h2>
         <form action="/echo_user_input" method="POST">
             <input name="user_input" type="text" placeholder="Type something...">
             <input type="submit" value="Submit">
         </form>
     </div>
     ''')

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return render_template_string(STYLE + '''
    <div class="container">
        <h2>You entered:</h2>
        <p style="background-color: #e7f4e4; padding: 20px; border-left: 6px solid #5cb85c;">{{ input_text }}</p>
        <a href="/">Go back</a>
    </div>
    ''', input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)

