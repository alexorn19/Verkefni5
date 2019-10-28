from flask import Flask, render_template, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(24)

vorur = [[0,"Nocco",300],[1,"RedBull",289],[2,"Monster",499]]

@app.route('/')
def index():
    session['user'] = 'Brask'
    return render_template("base.html", v=vorur)
    
@app.route('/getsession')
def getsession():
 if 'user' in session:
  return session['user']   

 return 'Not logged in!'
            
    
@app.route('/kaupa/<int:nr>')
def kaupa(nr):
	temp_karfa = []
	# er karfa tóm, ef satt þá ekki tóm?
	if 'karfa' in session:
		temp_karfa = session['karfa']
		temp_karfa.append(nr)
		session['karfa'] = temp_karfa
		return "Vara sett í körfu" 
	else:
		temp_karfa.append(nr)
		session['karfa'] = temp_karfa
		return "Fyrsta varan sett í körfu"
    

@app.route('/karfa')
def karfa():
	temp_karfa = []
	if 'karfa' in session:
		temp_karfa = session['karfa']
		return render_template('karfa.tpl',valdarvorur=temp_karfa, vorur=vorur)
	else:
		return "Karfan er tóm..."

@app.route('/ut')
def ut():
	return render_template('ut.html')
   



@app.errorhandler(404)
def error404(error):
 return '<h1>Síðan er ekki til!! <br><a href="/"> Smelltu Hér Til Að Komast Aftur Heim</a></h1>', 404
    
       
    

if __name__ == "__main__":
	app.run(debug=True)