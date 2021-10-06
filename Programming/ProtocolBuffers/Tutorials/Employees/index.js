// init array of employees
const employees = []

// add employees
employees.push({
    "name": "Hussein",
    "salary": 1000,
    "id": 1001
})

const ahmed = {
    "name":"Ahmed",
    "salary": 9000,
    "id": 1002,
}

employees.push(ahmed);
employees.push({
    "name": "Rick",
    "salary": 1000,
    "id":1003
})

employees.push({
    "name":"Rick",
    "salary": 1000,
})

// show in console
console.log(JSON.stringify(employees))

// write to desk to show size of file
const fs = require("fs");
fs.writeFileSync("jsondata.json",JSON.stringify(employees))
// enter ls -lh in terminal: 125B