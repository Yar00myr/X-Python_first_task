from flask import render_template, redirect, url_for, flash, jsonify
from .. import app
from ..forms import WashingMachineForm
from ..utils import WashingMachine


@app.get("/")
def get_washing_machine():
    form = WashingMachineForm()
    return render_template("washing_machine.html", form=form, result=None)


@app.post("/")
def washing_machine():
    form = WashingMachineForm()
    result = None

    if form.validate_on_submit():

        machine = WashingMachine()
        result = machine.start()
        flash(result["status"], "info")
        return redirect(url_for("washing_machine"))

    return render_template("washing_machine.html", form=form, result=result)


@app.get("/wash_status")
def wash_status():
    machine = WashingMachine()
    stages = []

    for stage in machine.start():
        stages.append(stage)

    return jsonify(stages)
