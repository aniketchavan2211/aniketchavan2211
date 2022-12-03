## HTML

### Syntax

```html
<!DOCTYPE html>
<html>

  ...

</html>

```

### IDEs and Text Editor

you use any text editor or IDEs
Example of IDEs: VSCode, Xcode, etc
Example of Text Editor: nano , vim, notepad, wordpad

### Head tag

```
<!DOCTYPE html>
<html>
  <head>
    <title> This is Title </title>

    <meta lang="en">
    <meta charset="UTF-8">
    <meta name="description" content="abc">
    <meta name="Author" content="Anonymous">
    <meta name="Location" content="Russia">
    <meta name="Date" content="3 Dec 20022"

    <link rel="stylesheet" href="style.css">

    <script src="script.js"> </script>

  </head>
</html>
```

<meta> tag : meta data

lang : language attribute
en : english
hi : hindi

link tag is link to `style.css` file

**style.css**
```css
body{
    background-color: black;
}
```

`rel` : relation
`href`: source of file / complete path / link

script tag is linked to `script.js` file

**script.js**
```javascript
alert("THis is alert from script.js file");
```

### Comment tag

comment are ignored save in file without show or executed
use for developer, ...


```html
<!-- 
  this will not show on website 
  or executed on website
 -->
```


### Body Tag

```html
<!DOCTYPE html>
<html>

<body>

  <p> ... <br> ... </p>

  <pre> ... </pre>

  <h1> Heading 1 </h1>
  <h2> Heading 2 </h2>
  <h3> Heading 3 </h3>
  <h4> Heading 4 </h4>
  <h5> Heading 5 </h5>
  <h6> Heading 6 </h6>

  <a href="https://www.google.com" target="_blank"> Link text  </a>
  <!-- tag, attribute, property -->

  <b> Bold Text </b> <B> Bold </B>
  <strong> Strong text </strong>
  <i> italic text </i>
  <em> empahasis text </em>
  <u> Underlined text </u>
  <mark> mark tag </mark>
  <small> small text </small>
  <bdo dir="rtl"> reverse text </bdo>
  <ins> inserted </ins>
  <del> delete text </del>
  <sup> superscript (upside)</sup>
  <sub> subscript (downside) </sub>
  <blockquote> quote  </blockquote>
  <q> text in quotes </q>

  <address> <pre>name phoneno. location</pre> </address>

  <abbr title="hint"> abbrivations <abbr>

  
</body>

</html>
```


`<p> </p>` : paragraph tag (ignore the space)
`<pre` `</pre>` : display as space is written
`<br>` : line break

`<h1>` to `<h6` : heading tag `h1` tag is larger than `h6`

`<a>` url `</a>` : anchor tag

`href` : hyper reference , source or url
`target` : `_self` will open page in same tab , `_blank` will open page in new tab, `_top` : will open in same tab.

`abbr` : title written text display when cursor on it.


### Image

```html
<!-- Image -->

  <img src="path/location" width="1024px" height="1024px">  

  <picture> 
    <source media="(min-width: 200px)" scrset="picture200px.png"> 
    <source media="(min-width: 400px)" scrset="photos400px.png"> 
    <source media="(min-width: 600px)" scrset="image600px.png">
    <img src="picture.png" style="width: auto;"> 
  </picture>

  <img src="picture.png" width"200px" height="200px" alt="error while loading" usemap="#iamgetut">
  <map name="imagetut">

    <area shape="rect" coords="111 11, 111 111" alt="ERROR" href="www.google.com" target="_blank"> 

    <!-- shape: cricle, default, poly, rect , imagemap.org-->

  </map>

  <embed src="image.png" type="image/png" width="100px" height="100px"> </embed>

```

### Tbale

```html
<table border="3px">
 
 <caption> Title </caption>

 <thead>
   <tr>

     <th> Name </th>
     <th> Model </th>
     <th> Year </th>
     <th> Driven </th>   

   </tr> 
 </thead>
 <tbody>
  <tr>
    <td> Maruti </td>
    <td> Switf </td>
    <td> 2018 </td>
    <td> 8234 </td>
  </tr>
  <tr>
    <td> Maruti </td>
    <td> Ciaz </td>
    <td> 2018 </td>
    <td> 8234 </td>
  </tr>
  <tr>
    <td> Maruti </td>
    <td> Wagonr </td>
    <td> 2018 </td>
    <td> <immg src="pic.png" width="100px" height="100px"></td>
  </tr>
 </tbody>

 <tfoot>
  <td> Total </td>
    <td> Gross </td>
    <td> Net </td>
    <td> Final </td>
 </tfoot>

</table>
```

**style.css**
```css
tbody{
  background-color: cornflowerblue;
  color: rgb(0, 0, 0);
}
table{
  padding: 25px;
}
```

### Iframe

```html
<html>
  
  <iframe src="url" height="500px" width="850px"> </iframe>

  <!-- PDFs -->
  <iframe src="pdf.pdf/path of pdfs"> </iframe>
  
  <embed src="pdf.pdf" type="application/pdf" width="100px" height="100px"> </embed>
  
  <object data="pdfs.pdf" type="application/pdf" width="100" height="100"> <\object>

</html>
```

### List

```
<!-- Ordered list <ol> -->
<ol type="1/ A/ a/ I/ i">

  Cars:
  <li> Hex </li>
  <li> Kai </li>
  <li> Ferrai </li>
  <li> Lambo </li>
  <li> Buggati </li>

</ol>

<ul type="disc/ square/ round"> 

  Cars:
  <li> BMW </li>
  <li> Audi </li>
  <li> Ferrai </li>
  <li> Lambo </li>
  <li> Buggati </li>

</ul>
<ul style="list-style: circle/...""> 

  Cars:
  <li> BMW </li>
  <li> Audi </li>
  <li> Ferrai </li>
  <li> Lambo </li>
  <li> Buggati </li>

</ul>
```


### Data list


```html
<dl> 
 <dt> Top Search engine </dt>
 <dd> Google </dd>
 <dd> Bing </dd>
 <dd> Yahoo </dd>
 <dd>  DuckDuckGo </dd> 
</dl>
```


### Symbols

Character enities

```html
<ul style="list-style: circle/...""> 

  Cars:
  <li> BMW </li>
  <li> Audi </li>
  <li> Ferrai </li>
  <li> Lykan&nbsp;Hpersport </li>
  <li> Buggati </li>

</ul>
```

`&nbsp;` : whitespace
`&copy;` : copyright

emoji enities code decimal value : 173634
```
&#173634;
```


### Audio

```html
<audio controls>
  <source src="audiofile.mp3" type="audio/mp3">
</audio>

```

### Video

```html
<video controls autoplay width="100" height="100">
  <source src="video.mp4" type="video/mp4">
</video>
```

### div tag (block element)

```
<div style="background-color: yellow;">
  <p> ... </p>
</div>

```

### span tag (inline element)

```
<span>
  <h1> THis is heading </h1>
</span>

```

### new HTML5 tags

```
<nav> </nav>
<article> </article>
<header> </header>
<footer> </footer>
<map> </map>
<summary> </summary>
<section> </section>
<aside> </aside>
<details> </details>
<textarea> </textarea>
```


### Form tag


```html

<div>
  <form methods="POST" action="file.php">
    <label> Registration </label>
      <input type="search" placeholder="Search">
      <input type="email">
      <input type="password">
      <input type="date">
      <input type="datetime">
      <input type="week">
      <input type="time">
      <input type="checkbox">
      <input type="radio">
      <input type="range">
      <input type="color">
      <input type="button">
      <input type="tel">
      <button name="Submit"> Press Me</button>
  </form>
</div>
```
