import svgpathtools
import matplotlib.pyplot as plt
import aspose.words as aw
import convertapi
import webbrowser


def complex(real, imag):
    return real + imag*1j


# Conversion
convertapi.api_secret = 'YXLO98UALYGS2GL4'
convertapi.convert('svg', {
    'File': r"C:\Users\Vigne\OneDrive\Desktop\istockphoto-1263601084-612x612.jpg"
}, from_format = 'jpg').save_files('output.svg')

# open output.svg and extract all the paths
paths, attributes = svgpathtools.svg2paths('output.svg')

# Initialization
doc = aw.Document()
builder = aw.DocumentBuilder(doc)

# get the image
imageLocation = input("Enter the location of the image: ")
shape = builder.insert_image(imageLocation)
shape.image_data.save("Output.svg")

# Parse the SVG path
path = svgpathtools.parse_path("Output.svg")
path = svgpathtools.parse_path("M3704 6128 c3 -79 10 -216 15 -305 8 -141 7 -351 -2 -1209 -2 -169 4 -194 44 -194 25 0 27 13 33 250 6 227 15 278 72 397 61 127 145 170 198 100 14 -18 33 -53 41 -78 19 -53 87 -329 111 -451 12 -65 23 -93 40 -109 22 -21 26 -22 40 -7 15 15 15 18 0 45 -8 15 -25 82 -36 148 -24 136 -68 313 -99 395 -71 189 -215 196 -335 15 l-26 -40 0 140 c-1 214 -17 584 -35 761 -8 88 -18 187 -21 222 -5 54 -8 62 -26 62 -21 0 -21 -3 -14 -142z M3046 5838 c-29 -818 -34 -1025 -26 -1158 5 -80 9 -155 9 -167 1 -27 31 -45 52 -33 11 8 14 38 14 152 0 132 2 147 25 191 28 56 96 122 145 143 19 8 55 14 81 14 40 0 51 -5 84 -37 66 -67 78 -188 23 -239 -59 -55 -138 -41 -239 41 -36 30 -70 55 -74 55 -4 0 -14 -7 -21 -16 -12 -15 -7 -23 41 -67 103 -93 206 -120 295 -77 58 28 85 79 85 161 0 102 -57 200 -133 228 -82 31 -199 -6 -276 -87 l-44 -47 6 425 c4 234 4 485 0 558 -5 116 -8 132 -23 132 -16 0 -18 -18 -24 -172z M2392 5938 c-6 -24 -15 -34 -31 -36 -22 -4 -23 -7 -17 -59 5 -46 1 -70 -25 -146 -36 -108 -149 -346 -221 -468 -48 -82 -53 -87 -114 -113 -46 -20 -64 -33 -64 -47 0 -21 21 -25 51 -9 38 21 18 -15 -97 -170 -92 -125 -205 -310 -202 -329 2 -9 13 -17 24 -19 17 -2 32 14 74 80 30 46 100 144 156 219 57 75 119 162 139 193 20 32 42 59 48 61 7 2 99 6 204 7 l193 3 11 -55 c24 -125 84 -341 119 -435 21 -55 40 -108 44 -118 4 -12 14 -17 28 -15 35 5 33 41 -5 148 -49 134 -134 493 -119 498 6 2 22 12 34 22 21 17 22 20 7 35 -14 14 -21 15 -39 5 -12 -6 -24 -10 -26 -7 -9 8 -154 592 -154 617 0 14 7 50 15 80 20 74 19 90 -5 90 -14 0 -22 -10 -28 -32z m44 -503 c30 -136 54 -253 54 -260 0 -10 -38 -14 -172 -17 -95 -2 -174 -3 -176 -2 -2 1 15 35 37 76 51 93 129 269 167 375 16 45 30 80 32 78 2 -2 28 -114 58 -250z M7330 5255 c0 -18 5 -25 20 -25 15 0 20 7 20 25 0 18 -5 25 -20 25 -15 0 -20 -7 -20 -25z  M5660 5182 c-56 -56 -86 -240 -57 -343 18 -59 72 -130 118 -154 98 -51 237 23 255 137 4 21 10 41 15 43 4 3 23 -23 41 -57 18 -34 56 -87 85 -118 43 -47 62 -59 110 -73 50 -14 60 -14 72 -2 21 21 1 39 -59 54 -59 15 -108 65 -160 163 -49 93 -77 128 -105 128 -30 0 -34 -7 -46 -81 -12 -78 -31 -115 -72 -140 -65 -41 -147 -4 -188 86 -22 47 -25 136 -8 233 14 82 37 107 88 98 59 -9 111 -85 111 -163 0 -16 6 -23 20 -23 45 0 15 146 -41 197 -56 51 -136 58 -179 15z M4923 5023 c4 -110 11 -165 26 -214 36 -115 106 -186 172 -177 l29 5 0 -108 c0 -114 -24 -368 -40 -429 -15 -57 -52 -105 -82 -108 -42 -5 -68 15 -96 76 -26 58 -27 67 -19 277 2 47 0 50 -22 50 -34 0 -42 -34 -44 -175 -2 -108 0 -119 27 -173 70 -144 203 -156 272 -25 40 76 73 324 79 592 2 89 7 229 10 311 7 157 0 218 -28 223 -8 2 -24 -9 -34 -24 -15 -23 -17 -52 -18 -215 0 -180 -1 -189 -22 -210 -21 -21 -23 -21 -47 -6 -29 20 -68 83 -89 148 -9 25 -21 109 -28 187 -12 130 -15 142 -32 142 -19 0 -20 -6 -14 -147z M4595 5150 c-86 -17 -138 -125 -139 -285 -1 -143 34 -205 108 -191 65 12 116 91 138 214 l11 67 16 -90 c18 -99 51 -165 82 -165 24 0 24 24 0 64 -10 17 -24 65 -30 106 -7 41 -14 87 -17 103 -5 22 -2 27 15 27 66 0 -36 143 -109 153 -19 3 -53 2 -75 -3z m108 -64 c23 -17 22 -25 -3 -19 -26 7 -35 -17 -54 -145 -19 -121 -35 -164 -71 -188 -25 -16 -27 -16 -43 0 -14 14 -17 37 -17 129 0 96 4 119 24 165 13 29 31 57 40 62 24 14 103 11 124 -4z M7852 5023 c-41 -20 -99 -86 -107 -122 -8 -38 21 -138 57 -198 17 -28 85 -109 151 -180 115 -124 153 -174 140 -187 -23 -22 -172 12 -257 60 -38 21 -49 24 -61 14 -23 -19 -19 -28 33 -60 94 -60 262 -92 319 -61 66 35 31 108 -136 284 -139 146 -191 227 -191 298 0 75 78 129 184 129 29 0 36 4 36 20 0 18 -7 20 -67 20 -42 0 -81 -7 -101 -17z M7493 4983 c2 -16 12 -62 21 -103 9 -41 26 -133 37 -204 18 -120 19 -130 3 -147 -14 -16 -15 -21 -4 -34 24 -29 50 -38 67 -23 20 17 13 94 -27 287 -43 212 -56 251 -81 251 -18 0 -20 -5 -16 -27z M6194 3742 c-21 -16 -82 -74 -134 -128 -72 -76 -108 -124 -149 -199 -30 -55 -67 -122 -83 -150 l-28 -50 0 86 c0 47 -3 147 -7 222 -5 121 -8 137 -23 137 -16 0 -19 -18 -25 -172 -3 -95 -5 -267 -3 -383 3 -208 3 -210 25 -213 27 -4 31 11 35 133 l3 90 74 130 c140 246 214 343 345 452 43 36 48 44 37 57 -18 21 -22 21 -67 -12z M6666 3450 c-47 -119 6 -353 100 -440 50 -46 87 -52 128 -19 l26 20 0 -143 c-1 -253 -24 -475 -56 -525 -40 -63 -215 6 -415 165 -81 64 -112 73 -117 37 -5 -39 269 -234 382 -271 100 -33 180 -14 210 51 46 96 51 156 51 625 0 432 -1 445 -19 448 -36 7 -46 -24 -46 -143 0 -163 -32 -249 -84 -229 -22 8 -72 87 -97 153 -24 61 -32 215 -15 279 8 28 6 32 -12 32 -14 0 -25 -12 -36 -40z M6372 3409 c-24 -12 -54 -38 -68 -58 -26 -39 -64 -148 -64 -186 0 -13 -7 -30 -15 -39 -16 -16 -20 -46 -6 -46 4 0 11 -33 13 -74 8 -122 57 -180 151 -180 97 0 188 77 266 225 36 68 37 99 2 99 -14 0 -31 -22 -61 -76 -93 -169 -204 -239 -271 -168 -20 22 -24 38 -28 105 l-3 79 44 0 c34 0 55 7 86 30 58 42 75 80 80 180 4 74 2 87 -14 102 -32 28 -65 30 -112 7z m74 -109 c-3 -38 -11 -81 -18 -95 -13 -28 -58 -59 -102 -69 l-29 -7 7 53 c15 107 68 188 124 188 25 0 25 0 18 -70z M3869 3386 c-36 -17 -77 -101 -90 -185 l-12 -74 -39 122 c-32 100 -42 121 -58 121 -27 0 -26 -12 15 -150 37 -129 57 -229 75 -386 17 -142 41 -183 76 -129 16 24 16 41 4 223 -13 213 -7 300 27 370 43 89 87 23 132 -199 34 -172 66 -282 85 -298 18 -15 43 -4 53 22 4 12 7 92 8 177 0 142 2 159 24 203 38 77 116 117 172 87 49 -27 86 -161 98 -363 8 -137 12 -147 62 -147 35 0 56 24 39 45 -7 8 -18 15 -25 15 -8 0 -14 33 -19 108 -12 187 -41 293 -97 356 -108 123 -298 -1 -317 -208 l-5 -60 -23 105 c-28 124 -46 174 -76 212 -29 34 -77 49 -109 33z  M5371 3389 c-82 -25 -146 -91 -178 -184 l-17 -50 -8 35 c-42 166 -50 190 -69 190 -11 0 -19 -7 -19 -16 0 -9 20 -107 44 -218 24 -110 47 -223 52 -251 7 -40 13 -51 31 -53 28 -4 36 23 32 107 -10 194 2 260 59 323 40 45 85 68 131 68 40 0 76 -45 91 -112 18 -88 32 -268 26 -345 -5 -60 -3 -75 13 -94 16 -20 21 -21 35 -10 13 11 16 36 16 140 0 233 -42 405 -110 453 -32 22 -86 29 -129 17z M4735 3310 c-15 -16 -16 -22 -5 -35 7 -9 21 -13 31 -10 13 4 26 -5 48 -35 53 -74 66 -129 66 -286 0 -128 -2 -144 -20 -164 -27 -30 -86 -22 -126 16 -43 41 -59 102 -59 224 0 120 12 170 41 170 13 0 19 7 19 21 0 17 -5 20 -32 17 -48 -5 -66 -38 -79 -147 -28 -234 46 -373 197 -373 48 0 82 26 106 79 18 41 20 61 16 187 -6 171 -25 232 -97 307 -51 53 -78 60 -106 29z M5920 3124 c0 -30 56 -130 95 -169 68 -68 205 -91 205 -34 0 16 -8 19 -42 19 -53 0 -118 29 -145 63 -11 14 -33 51 -49 81 -18 36 -35 56 -46 56 -10 0 -18 -7 -18 -16z")


"""
Take the bezier points from an SVG file and check what type of bezier 
equation they represent. Then construct bezier equations for each segment 
using compelx numbers. Convert the bezuer equaitons to graphable parametrics. 
Put them in latex format and then use the desmos API to create a viweable
HTML file that can be opened in the browser.
"""
eqns,regularEqns = [],[]
for segment in path:
    if isinstance(segment, svgpathtools.path.Line):
        start = complex(segment.start.real, segment.start.imag)
        end = complex(segment.end.real, segment.end.imag)
        #eqns.append("\left(" + str(start.real) + "+t*" + str(end.real) + ", " + str(start.imag) + "+t*" + str(end.imag) + "\\right)")

    elif isinstance(segment, svgpathtools.path.CubicBezier):
        # Cubic Bezier segment
        p0 = complex(segment.start.real, segment.start.imag)
        p1 = complex(segment.control1.real, segment.control1.imag)
        p2 = complex(segment.control2.real, segment.control2.imag)
        p3 = complex(segment.end.real, segment.end.imag)
        eqns.append("\\\\left((1-t)^3*" + str(p0.real) + "+3*t*(1-t)^2*" + str(p1.real) + "+3*t^2*(1-t)*" + str(p2.real) + "+t^3*" + str(p3.real) + ", (1-t)^3*" + str(p0.imag) + "+3*t*(1-t)^2*" + str(p1.imag) + "+3*t^2*(1-t)*" + str(p2.imag) + "+t^3*" + str(p3.imag) + ")\\\\right)")

    elif isinstance(segment, svgpathtools.path.QuadraticBezier):
        # Quadratic Bezier segment
        p0 = complex(segment.start.real, segment.start.imag)
        p1 = complex(segment.control.real, segment.control.imag)
        p2 = complex(segment.end.real, segment.end.imag)
        eqns.append("\\\\left((1-t)^2*" + str(p0.real) + "+2*t*(1-t)*" + str(p1.real) + "+t^2*" + str(p2.real) + ", (1-t)^2*" + str(p0.imag) + "+2*t*(1-t)*" + str(p1.imag) + "+t^2*" + str(p2.imag) + ")\\\\right))")

    elif isinstance(segment, svgpathtools.path.Arc):
        # Elliptical arc segment
        p0 = complex(segment.start.real, segment.start.imag)
        p1 = complex(segment.end.real, segment.end.imag)
        r = complex(segment.radius.real, segment.radius.imag)
        eqns.append("\\\\left(" + str(p0.real) + "+" + str(r.real) + "*\\cos(t), " + str(p0.imag) + "+" + str(r.imag) + "*\\sin(t)\\\\right)")

    else:
        print("Unknown segment type: " + str(type(segment)))


"""
Desmos API is used to plot the parametric equations in latex format.
The HTML code is then opened in the browser.
"""
# Desmos API
desmos = """<script src="https://www.desmos.com/api/v1.8/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
<div id="calculator" style="width: 1080; height: 720;"></div><script>
  var elt = document.getElementById('calculator');
  var calculator = Desmos.GraphingCalculator(elt);
"""
for i in range(len(eqns)):
    desmos += "calculator.setExpression({ id: 'a-slider" + str(i) + "', latex: '" + eqns[i]  + "' });\n"

desmos += "</script>"

# save the desmos file
f = open("desmos.html", "w")
f.write(desmos)
f.close()

# open the desmos file in the browser
webbrowser.open("desmos.html", new=2)
