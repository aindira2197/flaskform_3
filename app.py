from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])   
def reault():
    if request.method == 'POST':
        n = request.form.get('kitob_nomi')
        m = request.form.get('muallif')
        s = request.form.get('sahifalar')
        s = int(s)

        if len(n) > 3 and len(m) > 3 and s >= 50:
            res = [n, m, s]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

        return render_template('res.html', res=res)
    
    return render_template('index.html')
    




if __name__ == '__main__':
    app.run(debug=True)
