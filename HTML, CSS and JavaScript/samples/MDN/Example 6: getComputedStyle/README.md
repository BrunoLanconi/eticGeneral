# Example 6: getComputedStyle

This example demonstrates how the window.getComputedStyle method can be used to get the styles of an element that are not set using the style attribute or with JavaScript (e.g., elt.style.backgroundColor="rgb(173, 216, 230)"). These latter types of styles can be retrieved with the more direct elt.style property, whose properties are listed in the DOM CSS Properties List.

getComputedStyle() returns a CSSStyleDeclaration object, whose individual style properties can be referenced with this object's getPropertyValue() method, as the following example document shows.

[MDN Example](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Examples#example_6_getcomputedstyle)