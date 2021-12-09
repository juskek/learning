# React
- Framework for UI 
  - View component of MVC
## Features
- Reusable dynamic components
  - Holds state
- JSX
  - Dynamic HTML with JS expressions
- Interactive UIs with Virtual DOMS
  - Target specific components to update

## Components
### Types
- Can be created as 
  - function component, e.g., `export const Header = () => {return ...}`
    - less overhead
  - class component, e.g, `export default class Header extends React.Component {render() {return ...}}`
    - provides base functions like render 
### Usage
- Can be embedded in html
  - e.g., `<Header props="propName"/>`
    - props can be passed as arguments to the component
### State
- Objects to define behaviour
  - e.g., menu open/close
- Storing state
  - Class component 
  - Hooks
    - allows usage of state in other lifecycle components within function components
- Scope
  - App/global: state available to entire UI
  - Local: state available to component only
- Notes
  - Passing state with context API possible

## Hooks
- Functions that hooks into React state and lifecycle features from function components

### useState
- Returns stateful value and function to update it
### useEffect
- Perform side effects in function components
- e.g., 
  - HTTP requests when loading page
### useContext

### useReducer

### useRef

### Custom

## Structure
- public/index.html describes the homepage
  - Single page app, any other URL is routed via React
  - Root element in body
- src/index.js renders App.js into the root element of index.html 
- App.js returns components depending on path