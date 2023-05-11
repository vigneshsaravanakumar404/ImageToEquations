# Modules
import re
import webbrowser

import numpy as np
import svgpathtools
from svgpathtools import Line, CubicBezier

# !ENTER FILE LOCATION HERE, SVGs only https://convertio.co/png-svg/
file = open(r"C:\Users\Vigne\Downloads\download-_6_ (1).svg", "r")
data = str(file.read()).replace('fill="#000000" opacity="1.000000" stroke="none"', "")
file.close()


# Functions
def _tokenize_path(pathfinder):
    FLOAT_RE = re.compile("[-+]?[0-9]*\.?[0-9]+(?:[eE][-+]?[0-9]+)?")
    for x in re.compile("([MmZzLlHhVvCcSsQqTtAa])").split(pathfinder):
        if x in set("MmZzLlHhVvCcSsQqTtAa"):
            yield x
        for token in FLOAT_RE.findall(x):
            yield token


def aplusbiFormat(real, imaginary):
    return real + imaginary * 1j


def extract_path(pathfinder, current_pos=0j):
    # Variables
    elements = list(_tokenize_path(pathfinder))
    elements.reverse()
    segments = []
    start_pos = None
    command = None

    # Loop through all the paths
    while elements:
        if elements[-1] in set("MmZzLlHhVvCcSsQqTtAa"):
            command = elements.pop()
            absolute = command in set("MZLHVCSQTA")
            command = command.upper()
        else:
            if command is None:
                raise ValueError("idk what happened so im just gonna say error. Error!")

        if command == "M":
            x = elements.pop()
            y = elements.pop()
            pos = float(x) + float(y) * 1j
            if absolute:
                current_pos = pos
            else:
                current_pos += pos
            start_pos = current_pos
            command = "L"

        elif command == "Z":
            if not (current_pos == start_pos):
                segments.append(Line(current_pos, start_pos))
            current_pos = start_pos
            command = None

        elif command == "L":
            x = elements.pop()
            y = elements.pop()
            pos = float(x) + float(y) * 1j
            if not absolute:
                pos += current_pos
            segments.append(Line(current_pos, pos))
            current_pos = pos

        elif command == "C":
            control1 = float(elements.pop()) + float(elements.pop()) * 1j
            control2 = float(elements.pop()) + float(elements.pop()) * 1j
            final = float(elements.pop()) + float(elements.pop()) * 1j

            if not absolute:
                control1 += current_pos
                control2 += current_pos
                final += current_pos

            segments.append(CubicBezier(current_pos, control1, control2, final))
            current_pos = final

    return segments


# get all the text in between the <path and ></path>
pathArray = re.findall(r'<path d="(.*?)"', data, re.DOTALL)

pathString = ""
for path in pathArray:
    pathString += path

path = extract_path(pathString)

equations, regularEquations = [], []
for segment in path:

    # Iterate through each segment, a set of 4 points, in the SVG file and check what type of segment it is
    if isinstance(segment, svgpathtools.path.Line):

        # Extract the start and end points from the line segment
        start = aplusbiFormat(segment.start.real, segment.start.imag)
        end = aplusbiFormat(segment.end.real, segment.end.imag)

        if end.real - start.real != 0:
            # calculate the slope and y-intercept of the line segment
            m = (end.imag - start.imag) / (end.real - start.real)
            b = start.imag - m * start.real

            # calculate the bounds of the line segment in the x direction
            xMin = min(start.real, end.real)
            xMax = max(start.real, end.real)

            # calculate the bounds of the line segment in the y direction
            yMin = min(start.imag, end.imag)
            yMax = max(start.imag, end.imag)

            # Convert the linear equation into the form y=mx+b and put it in latex format

        equations.append(
            "y="
            + str(m)
            + "x+"
            + str(b)
            + "\\\\left\\\\{"
            + str(xMin)
            + "\\\\le x \\\\le "
            + str(yMin)
            + "\\\\right\\\\}\\\\left\\\\{"
            + str(yMin)
            + "\\\\le y \\\\le "
            + str(yMax)
            + "\\\\right\\\\}"
        )
        # equations.append(f"y={m}x+{b}\\left\\{{{xMin} \\le x \\le {xMax}\\}}\\right\\}}\\left\\{{{yMin} \\le y \\le {yMax}\\}}\\right\\}}")
        equations.append(
            "y="
            + str(m)
            + "x+"
            + str(b)
            + "\\\\left\\\\{"
            + str(xMin)
            + "\\\\le x \\\\le "
            + str(yMin)
            + "\\\\right\\\\}\\\\left\\\\{"
            + str(yMin)
            + "\\\\le y \\\\le "
            + str(yMax)
            + "\\\\right\\\\}"
        )

        print(
            f"y={m}x+{b}\\left\\{{{xMin} \\le x \\le {xMax}\\}}\\right\\}}\\left\\{{{yMin} \\le y \\le {yMax}\\}}\\right\\}}"
        )

        # Convert the linear equation into the form y=mx+b and put it in lambda format
        regularEquations.append(lambda x: m * x + b)

    elif isinstance(segment, svgpathtools.path.CubicBezier):

        # extract the bezier points from the segment
        p0 = aplusbiFormat(segment.start.real, segment.start.imag)
        p1 = aplusbiFormat(segment.control1.real, segment.control1.imag)
        p2 = aplusbiFormat(segment.control2.real, segment.control2.imag)
        p3 = aplusbiFormat(segment.end.real, segment.end.imag)

        # Convert the bezier points into a parametric equation in latex format
        equations.append(
            "\\\\left((1-t)^3*"
            + str(p0.real)
            + "+3*t*(1-t)^2*"
            + str(p1.real)
            + "+3*t^2*(1-t)*"
            + str(p2.real)
            + "+t^3*"
            + str(p3.real)
            + ", (1-t)^3*"
            + str(p0.imag)
            + "+3*t*(1-t)^2*"
            + str(p1.imag)
            + "+3*t^2*(1-t)*"
            + str(p2.imag)
            + "+t^3*"
            + str(p3.imag)
            + ")\\\\right)"
        )

        # Convert the bezier points into a parametric equation in lambda format
        regularEquations.append(
            lambda t: (1 - t) ** 3 * p0
                      + 3 * t * (1 - t) ** 2 * p1
                      + 3 * t ** 2 * (1 - t) * p2
                      + t ** 3 * p3
        )

    elif isinstance(segment, svgpathtools.path.QuadraticBezier):
        # Quadratic Bezier segment
        p0 = aplusbiFormat(segment.start.real, segment.start.imag)
        p1 = aplusbiFormat(segment.control.real, segment.control.imag)
        p2 = aplusbiFormat(segment.end.real, segment.end.imag)

        # Convert the bezier points into a parametric equation in latex format
        equations.append(
            "\\\\left((1-t)^2*"
            + str(p0.real)
            + "+2*t*(1-t)*"
            + str(p1.real)
            + "+t^2*"
            + str(p2.real)
            + ", (1-t)^2*"
            + str(p0.imag)
            + "+2*t*(1-t)*"
            + str(p1.imag)
            + "+t^2*"
            + str(p2.imag)
            + ")\\\\right))"
        )

        # Convert the bezier points into a parametric equation in lambda format
        regularEquations.append(
            lambda t: (1 - t) ** 2 * p0 + 2 * t * (1 - t) * p1 + t ** 2 * p2
        )

    elif isinstance(segment, svgpathtools.path.Arc):
        # Elliptical arc segment
        p0 = aplusbiFormat(segment.start.real, segment.start.imag)
        p1 = aplusbiFormat(segment.end.real, segment.end.imag)
        r = aplusbiFormat(segment.radius.real, segment.radius.imag)

        # Convert the bezier points into a parametric equation in latex format
        equations.append(
            "\\\\left("
            + str(p0.real)
            + "+"
            + str(r.real)
            + "*\\cos(t), "
            + str(p0.imag)
            + "+"
            + str(r.imag)
            + "*\\sin(t)\\\\right)"
        )

        # Convert the bezier points into a parametric equation in lambda format
        regularEquations.append(lambda t: p0 + r * np.exp(1j * t))

    else:
        print("Unknown segment type: " + str(type(segment)))

# Define the Desmos API script
desmos = """
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://www.desmos.com/api/v1.8/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
<div id="calculator" style="width: 100%; height: 100%;"></div>
<script>
 var elt = document.getElementById('calculator');
 var calculator = Desmos.GraphingCalculator(elt);
"""

# use numpy to find the bounds of the graph


# Add the bounds to the Desmos API script
desmos += (
        "calculator.setMathBounds({ left: "
        + str(-194.97)
        + ", right: "
        + str(8852.635)
        + ", bottom: "
        + str(-221.556)
        + ", top: "
        + str(6152.893)
        + " });\n"
)

# Add each equation to the Desmos API script
for i in range(len(equations)):
    desmos += (
            "calculator.setExpression({ id: 'a-slider"
            + str(i)
            + "', latex: '"
            + equations[i]
            + "', color: Desmos.Colors.BLACK });\n"
    )
desmos += "</script>"

# Save and open Desmos file
with open("desmos.html", "w") as f:
    f.write(desmos)
webbrowser.open("desmos.html", new=2)

# TODO:
# Create demo video
# Create tkinter GUI
# Explain the math
# Comment the code
# Improve the README.md
# Clean up Github Profile
