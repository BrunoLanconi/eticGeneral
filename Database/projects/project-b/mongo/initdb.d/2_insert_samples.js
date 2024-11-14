db.samples.insertMany([
  {
    name: 'Sample1',
    values: [
      {
        name: 'inner-value-1',
        inner_value: 1,
      },
      {
        name: 'inner-value-2',
        inner_value: 2,
      },
      {
        name: 'inner-value-3',
        inner_value: 3,
      },
    ]
  },
  {
    name: 'Sample2',
    values: [
      {
        name: 'inner-value-4',
        inner_value: 4,
      },
      {
        name: 'inner-value-5',
        inner_value: 5,
      },
      {
        name: 'inner-value-6',
        inner_value: 6,
      },
    ]
  },
]);