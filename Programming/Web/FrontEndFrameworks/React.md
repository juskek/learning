# React
- Framework for UI 
  - View component of MVC
## Features
- Reusable dynamic components
  - Holds state
- JSX
  - Dynamic HTML with {JS expressions}
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
  - e.g., `<Header propsName="value"/>`

### Props
- props can be passed as arguments to the component
  - e.g., `const Header = (props) => {return <h1> {props.propsName}</h1>}`
- Props can be destructured
  - e.g., `const Header = ({prop1, prop2}) => {return <h1> {prop1} {prop2}</h1>}`
- Default props can be specified
  - e.g., `Header.defaultProps = {propsName: 'value'}`
- Prop types can be specified
  - e.g., `Header.propTypes = {propsName: PropTypes.string.isRequired}`
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

#### Prop Drilling
- State defined in App.js
  - Process
    1. Define function which manipulates state in App.js
    2. Pass it down to component where desired event occurs using props
       - e.g., `const functionName = (arg) => {...}`, 
       - `<Component propName = {functionName}>`, 
       - `const Component = (props) => {return <Button onEvent = {props.functionName}>`
- State gets passed down through props, actions get passed up to update state
## Events
- Events are stored in App.js
  - Can be passed down to components via 
    - props 
    - redux API

### onChange
- Value of element changed
- Handling of event: `onChange = {(e) => function(...)}`
## Hooks
- Functions that hooks into React state and lifecycle features from function components

### useState
- Allows usage of state in function
- Returns stateful value and function to update it
- Syntax:
  ```
  const Function = () => {
    // declare state and function to update state
    // initialise state
    const [stateName, setState] = useState(initialState) 
    // init function to update state 
    setState(newState)

    return ...
  }
### useEffect
- Perform side effects in function components
- e.g., 
  - HTTP requests when loading page
### useContext

### useReducer

### useRef

### Custom
## Styling
### Style Sheet: index.css
- template styles for entire app
- Defined as:
  ```
  .styleName {
    property: value;
  }
  ```
- Utilised as: `<div className = 'styleName'>`


### Style Components

### Direct JS CSS
- Double curly braces for in line styling, e.g., `style={{color: 'red'}}`
- Single curly braces otherwise, e.g., `const headingStyle = {color:'red'}` and `style = {headingStyle}`



## Structure
- public/index.html describes the homepage
  - Single page app, any other URL is routed via React
  - Root element in body
- src/index.js renders App.js into the root element of index.html 
- App.js returns components depending on path
- index.css 
### components/
- Uppercase for components filenames