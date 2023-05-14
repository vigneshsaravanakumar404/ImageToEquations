<style>
    body {
        margin: 100px;
    }
</style>

# Image to Equation

<a href="https://imgur.com/3dMZQ2l"><img src="https://i.imgur.com/3dMZQ2l.png" title="source: imgur.com" /></a>

## Example Outputs

SBHS Logo https://www.desmos.com/calculator/fbou42kptf

![img3.png](Images/sbhsvikings.png)

Computer science club logo:  https://www.desmos.com/calculator/dv4rccpeai

![img2.png](Images/cslogo.png)

750Royals Logo: https://www.desmos.com/calculator/wjrwpiiese

![img4.png](Images/royalslogo.png)

Rick Astley: https://www.desmos.com/calculator/lqt7ojodrm

![img5.png](Images/rickastely.png)

Spider Man (Lag Warning): https://www.desmos.com/calculator/izdfc0qpm2

![img.png](Images/spiderman.png )

*_For some graphs the original image is included on the right for reference, program generated output is on the left,
The image is not part of the computer generated output_*

## How It Works

This program converts an image into a set of grapahble equations, that are then displayed on desmos. The program
takes advantage of a file format called SVG (Scalable Vector Graphics). Unlike other methods of encoding images, like
PNG
and JPEG, SVG files store the image using mathematical equations instead. For this reason SVG files are very compact
and often used in 2D website design. Even android studios makes use of it for storing icons. Below is an example of an
SVG file that represent Python's logo.

```svg
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN"
        "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
     width="2000.000000pt" height="1270.000000pt" viewBox="0 0 2000.000000 1270.000000"
     preserveAspectRatio="xMidYMid meet">
    <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="m14.31.18.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.
   21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.83l-.69.05-.59.14-.5.22-.41.27-.
   33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.23l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.
   26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05L0 11.97l.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.
   44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.24l-.01-2.75-.02-.37.05-.34.11-.31.17
   -.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05 1.07.13zm-6.3 1.98-.23.
   33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09-.33
   .22zM21.1 6.11l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.
   24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-
   .05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.
   14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.
   21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.
   33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25-.23.33-.08.41.08.
   41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08-.33.23z"/>
    </svg>
```

<img src="Images/img.png" width="150" height="150">

## Demo

**to do include demo video**
<div align="center">
  <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley">
    <img src="https://i.imgur.com/vKb2F1B.png" alt="Watch the video">
  </a>
</div>

## Installation

```bash
  pip install svgpathtools
  pip install svgpathtools
  pip install numpy
```

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
     <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/59059d9d1a2c092696dc66e00931cc1181a4ce1f/icons/Idea-Dark.svg" width="64" height="64" alt="IntelliJ IDEA icon">
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






