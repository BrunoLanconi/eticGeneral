db.users.drop();

db.createCollection("samples", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["name", "values"],
      properties: {
        name: {
          bsonType: "string",
          uniqueItems: true
        },
        values: {
          bsonType: "array",
          items: {
            bsonType: "object",
            required: ["name", "inner_value"],
            properties: {
              name: {
                bsonType: "string",
              },
              inner_value: {
                bsonType: "number",
              }
            }
          }
        }
      }
    }
  }
});
