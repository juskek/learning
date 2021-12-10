# CSS
- Webpage styling

```
selector {
    prop: value;
}
```


## Selectors

### elements
- apply to specific HTML elements
- e.g., h1, div, header, btn
### class
- apply to HTML elements with same class attribute
- e.g., 
  - HTML: `<h1 class = "class-name">`
  - CSS: `.class-name {prop:value}`
- Can have multiple classes
  - separated by space
  - e.g., `<h1 class = "class1 class2">
- Can have base class and subclasses to overwrite specific properties 
### id
- apply to HTML elements with same id attribute
- Can only have one id attribute
- e.g., 
  - HTML: `<h1 class = "id-name">`
  - CSS: `#id-name {prop:value}`

### Selector Combinations
- Combine selectors: without space
  - e.g., `.selector1.selector2 {...}`
- Ancestor Child: with space
  - e.g., `.ancestor .child {...}`
- Duplicate selectors with same properties: use comma
  - e.g., `.selector1, .selector2
- All elements: *
  - e.g., for fonts

## Loading Styles
### Inline
- Defined in element
- Element scope
- May be slower if repeated inline styles are used

### Style Element
- Defined in head
- Page scope

#### External CSS
- Defined in .css and added in head
  - e.g., `link rel="stylesheet" href="style.css"/>`
- Global scope