# Image to Equation

## Screenshots

<a href="https://imgur.com/3dMZQ2l"><img src="https://i.imgur.com/3dMZQ2l.png" title="source: imgur.com" /></a>



Images to Include:
// Computer science club logo
// Rick astely 
// Some anime image
// Gemotric Shape
// CS Logo



## How It Works
Images are taken in and converted to an SVG (Scalable Vector Graphics). Unlike other forms of images, SVGs encode images in terms of mathematical equations. Specifically SVGs store images in the form of coordinate pairs that are converted into bezeir curves. The Bezier curves are defined by four points. Two coordinates define the start and ending position of the curve. The other two coordinates determine the concavity of the bezier curve. The Bezier curves are converted into a set of parametric equations that are easily graphable. This program extracts the bezier points from the SVG asset then uses linear interpolation to convert to parametric equations. Then desmos's API is used to graphically visualize the equations.   

## Built With
<table>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/59059d9d1a2c092696dc66e00931cc1181a4ce1f/icons/Python-Dark.svg" width="64" height="64" alt="Python">
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/59059d9d1a2c092696dc66e00931cc1181a4ce1f/icons/Gradle-Dark.svg" width="64" height="64" alt="Gradle icon">
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/59059d9d1a2c092696dc66e00931cc1181a4ce1f/icons/Idea-Dark." width="64" height="64" alt="IntelliJ IDEA icon">
    </td>
    <td align="center">
      <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/59059d9d1a2c092696dc66e00931cc1181a4ce1f/icons/SVG-Dark.svg" width="64" height="64" alt="SVG">
    </td>
  </tr>
</table>


## Acknowledgements

 - [Desmos API](https://www.desmos.com/api/v1.8/docs/index.html)
 - [SVG Graphics Explanation](https://developer.mozilla.org/en-US/docs/Web/SVG)
 - [SVG Documentation](https://www.w3.org/2000/svg)
  - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)


