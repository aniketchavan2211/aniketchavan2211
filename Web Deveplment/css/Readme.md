## CSS (Cascading Style Sheet)

- Use to add animations, graphics , dynamics, colors, borders, etc.

- `.css` extension

- Opening `/*` and closing `*/` Comments.

### inline style tag

style attr

```html
<p style="font-size: xx-large;"> Paragraph</p>
```

`<p>` : paragraph tag 
`style` : style attibute 
`font-size` : properties properties-value;
`:` : to assigned value to properties
`xx-large` : properties value
`:` : semicolon `:` end of statement

### Internal style sheet

```html

<style>

p{
  font-family: cursive;
  color: blue;
}

</style>
```

### External style sheet

```index.html
<link type="text/css" rel="stylesheet" href="style.css">
```

link `style.css` to `index.html` page
if not linked will not show the changes according to style.css

```style.css
body{
     background-image: url(image.jpg); /*image background loaction or path or image name with extension in url() */
     background-color: green; /* green color background */
     background-size: inherit; /* size change */
     background-repeat: no-repeat; /* backgorund will not repeat once display (if screen unfit image remanining will not cover with multiple images) */
     background-attactment: fixed; /* background will not move or not scroll, background fixed. */
}
```


### Selector

1. simple selector

```
body {
 ...
}
```

2. combination selector

```

```

3. pseudo class selector


```index.html
<div class="div1">
  <h1> Class Selector</h1>
</div>
```

```style.css
.classname{
 properties: values;
}

.div1{
 color: red;
}
```

properties will applied only on those classes name
which are mention in tag.

4. peseudo id selector

```index.html

<h1 id="tgt"> Heading </h1>

```

```style.css
#tgt{
  color: yellow;
}
```

#id-name {properties...}

properties only appered on mention id.

5. Attribut selector

```index.html
<a href="www.google.com" target="_blank"> Google </a>
<a href="www.google.com"> Google </a>
```

```style.css
a[target="_blank"]{
   color: maganeta;
}
```

first color will be magneta and second will not.

### Text

```style.css
p{
   color: #ffffff; white hexadecimal
   color: #ff0000; red 
   color: #00ff00; green
   color: #0000ff; blue
}
```

<p> tag is selected, you can give hexadecimal values as color

```
p{
  color; green;
}
```
simple write name color


```
p{
  color: rgb(00, 100, 00) /* Red Green Blue */
}
```

```
p{
  color: hsl(15%, 96% 52%);
}
```

hsl : hue, saturation, lightness

### Font

```
font-size: large; /* 85px */
font-weight: bolder;
font-family: cursive;
opacity: 0.9;
font-style: italic;
```

### image

```index.html
<img id="omg1" src="https://wallpaper.com/image.png">
```

```style.css
#img1{
  height: 631px;
  width: 794px;
  oparcity; 0.5:
  transition: 0.8s ease-in;
  border: 5px solid #ffffff;
  border-radius: 6px;
  border-width: 24px;
  border-style: dotted;
  border-spacing: 5px;
  margin-top: 25px;
  margin-left: 67px;
  margin-bootom: 11px;
  margin-right: 11px;
  margin: 25px; /* same 25px for all sides */
  padding-top: 20px; /* right left bottom */
  padding: 20px;
}
#img1:hover{
  height: 900px;
  width: 900px;
  oparcity; 1:
}
```

### Animation

```style.css
body{
  background-image: url(iamge.png); 
  animation-name: bgchnage;
  animation-duration: 3s;
  animation-iteration-count: infinite; /* 2 iter */
}

@keyframes bgchange{
  0%{background-image: url(image.png); width: 30px;}
  25%{background-image: url(image2.png);}
  50%{background-image: url(image2.png);}
  75%{background-image: url(image3.png);}
  100%{background-image: url(image4.png);}
}
```


### Gifs
