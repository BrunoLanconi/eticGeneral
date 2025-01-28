db.students.drop();

db.createCollection("students", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "registration"],
      properties: {
        name: {
          bsonType: "string",
          description: "must be a string and is required"
        },
        registration: {
          bsonType: "date",
          description: "must be a date and is required"
        }
      }
    }
  }
});