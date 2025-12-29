from flask import Flask, render_template

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/periode1")
def periode1():
    return render_template(
        "periode1.html", title="L'hégémonie imposée (1945-1960)"
    )


@app.route("/periode2")
def periode2():
    return render_template(
        "periode2.html", title="L'hégémonie autoritaire (1960-1987)"
    )


@app.route("/periode3")
def periode3():
    return render_template(
        "periode3.html", title="L'hégémonie démocratique (1987-2000)"
    )


@app.route("/periode4")
def periode4():
    return render_template(
        "periode4.html", title="L'hégémonie négociée (2000-2020)"
    )


@app.route("/ressources")
def ressources():
    return render_template("ressources.html", title="Sources et ressources")


@app.route("/jeju")
def jeju():
    return render_template("jeju.html", title="Le massacre de Jeju")


@app.route("/conclusion")
def conclusion():
    return render_template("conclusion.html", title="Conclusion")


@app.route("/interview")
def interview():
    return render_template("interview.html", title="Interview avec Eom Hyunsoo")


if __name__ == "__main__":
    app.run(debug=True)