from datetime import datetime
import pytz

from pywebio.output import put_row, put_column, put_text
from pywebio.pin import put_checkbox, pin_on_change, put_input


def def_lable_checkbox(component):
    for v in component.spec["input"]["options"]:
        v["label"] = ""
    return component


def explain_componet(texts, component):
    text_components = []
    for k, v in enumerate(texts):
        if k > 0:
            text_components.append(put_text(v).style("font-size:14px"))
        else:
            text_components.append(put_text(v))

    return put_row(
        [
            put_column(text_components).style("display:block;"),
            component,
        ]
    ).style("margin-bottom:15px;")


def render_checkbox(taksname, explaintext, checkboxkey, props, updatecheckbox):
    explain_componet(
        [explaintext],
        def_lable_checkbox(
            put_checkbox(checkboxkey, options=[True], value=props[checkboxkey])
        ),
    )
    pin_on_change(
        checkboxkey,
        onchange=lambda v: updatecheckbox(taksname, checkboxkey, v),
        clear=True,
    )


def render_input(taksname, explaintext, inputkey, props, inputfn):
    explain_componet(
        [explaintext],
        put_input(inputkey, value=props[inputkey]),
    )
    pin_on_change(
        inputkey, onchange=lambda v: inputfn(taksname, inputkey, v), clear=True
    )


def formatdate(v):
    v = datetime.fromisoformat(v).replace(tzinfo=pytz.UTC)
    ts = v.timestamp()
    return int(ts)


def render_number(taksname, explaintext, inputkey, allprops, numberfn):
    explain_componet(
        [explaintext],
        put_input(inputkey, value=allprops[inputkey], type="number"),
    )
    pin_on_change(
        inputkey, onchange=lambda v: numberfn(taksname, inputkey, v), clear=True
    )


def render_datetime(
    taksname, explaintext, inputkey, allprops, datetimefn, formatfn=formatdate
):

    explain_componet(
        [explaintext],
        put_input(inputkey, value=allprops[inputkey], type="datetime-local"),
    )
    pin_on_change(
        inputkey,
        onchange=lambda v: datetimefn(taksname, inputkey, formatfn(v)),
        clear=True,
    )
