from flask import Flask, redirect, url_for, request, render_template, Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from city_mapper_web import CityMapper


app = Flask(__name__)


@app.route("/map/<name>")
def map(name):
    cm = CityMapper.CityMapper()

    cm.load_data_from_city(
        city_name=name,
        city_limits=True,
        city_elements={"buildings": True, "green": True, "water": False},
    )

    fig = cm.plot_map(
        road_cycleway_ratio_subtitle=True, edge_width={"roads": 0.75, "cycleways": 2.5}
    )

    output = io.BytesIO()

    FigureCanvas(fig).print_png(output)

    return Response(output.getvalue(), mimetype="image/png")


@app.route("/input", methods=["POST", "GET"])
def input():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("map", name=user))
    else:
        return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
