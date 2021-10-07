// ProtoBuf Compiler
// converts proto file into JS file 
// which builds Employee and Employees classes

// import schema
const Schema = require("./employees_pb")

const hussein = new Schema.Employee();
hussein.setId(1001)
hussein.setName("Hussein")
hussein.setSalary(1001)


const ahmed = new Schema.Employee();
ahmed.setId(1002)
ahmed.setName("Ahmed")
ahmed.setSalary(9000)

const rick = new Schema.Employee();
rick.setId(1003)
rick.setName("Rick")
rick.setSalary(5000)

// Create array
const employees = new Schema.Employees();
employees.addEmployees(hussein)
employees.addEmployees(ahmed)
employees.addEmployees(rick)

// Serialize with protobuf
const bytes = employees.serializeBinary()
console.log("object " + employees)

console.log("binary " + bytes)

// Write to disk and compare size
const fs = require("fs")
fs.writeFileSync("employeesBinary",bytes)

// ls -lh
// almost three times smaller as compared to json

// deserialisation is also possible
const employeesDeserialized = Schema.Employees.deserializeBinary(bytes)

console.log("deserialised " + employeesDeserialized)
console.log(employeesDeserialized)