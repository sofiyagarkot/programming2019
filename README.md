This module is created for discovering the places on the map depending on the year, that user had typed.
The resulting file - Sofia.html is a map with 4 layers. User can manager which of the layers to display.
The first layer is the map itself.
The second layer are coloured countries depending on the population.
All of the countries are coloured in green, orange or red colours : if the population is more than 20000000 the colour is red; if population is between 10000000 and 20000000 - orange, and if the population is less than 10000000 - green.
The third layer are the blue markers, that show tha places where certain movies were being filmed. Notice that for reducing working time, there are only 500 of them. 
Clicking on it user can find out name of film, that was filmed on some place.
The fourth layer are circle markers. With circle markers are marked the areas, where several films were filmed.
Clicking on the circle marker user can see the number of films, that were filmed on some area. Circle marker is red if on the location were filmed more than 20 movies; yellow if the number of movies is between 5 and 20, and green if the number is less than 5.
Notice that for reducing the working time of the program there are only 1000 points on the map.
While working with module user will be asked to enter the year, when he or she wants to find out locations of movies.

The structure of the html-file (Sofia.html)
<!DOCTYPE html> - this tag is document type declaration. It is an instruction to the web browser about what version of HTML the page is written in.
<head> - The <head> element is a container for metadata (data about data) and is placed between the <html> tag and the <body> tag.
<meta http-equiv="content-type" content="text/html; charset=UTF-8" /> - The <meta> tag provides metadata about the HTML document. The http-equiv attribute provides an HTTP header for the information/value of the content attribute; content - gives the value associated with the http-equiv or name attribute; charset=UTF-8 is a character encoding.  
<script> - The <script> tag is used to define a client-side script (</script> - closing tag) .
<script src="..."></script> - The src attribute specifies the URL of an external script file.
<link> - The <link> element is used to define a relationship between an HTML document and an external resource. This element is most commonly used to define the relationship between a document and one or more external CSS stylesheets.
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.3.4/dist/leaflet.css"/> : rel - Specifies the relationship between the current document and the linked document; href - Specifies the location of the linked document.
<style> - The <style> tag is used to define style information for an HTML document. Inside the <style> element I specified how HTML elements should render in a browser. Each HTML document can contain multiple <style> tags.
<style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style> - full screen width to work
<style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style> - full screen map
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" /> - A <meta name="viewport"> viewport element gives the browser instructions on how to control the page's dimensions and scaling; 
<style>#map_d8f5bb9f91294d81b4c52066443a61e5{
        position: relative;
        width: 100.0%;
        height: 100.0%;
        left: 0.0%;
        top: 0.0%;
        }
    </style> - adding styled map at some position
</head> - closing head tag
<body> -  tag defines the document's body.
<div> tag defines a division or a section in an HTML document.
<div class="folium-map" id="map_d8f5bb9f91294d81b4c52066443a61e5" ></div> - class="folium-map" defines styles for elements.
</body> - closing body tag

This map illustrates the locations of films and the number of movies, that were filmed on some location.
On current map are illustrated data for films, that were filmed in 2015.
For example in Canada, Quesnel, Front street were filmed 5 films. The film "A is for Apple" was filmed in Canada, Ottawa.
Each of the circle markers is red, yellow or green, depending on number of movies, that were made on this location.