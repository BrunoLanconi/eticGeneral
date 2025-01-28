db.users.insertMany([
  {
    name: 'User1',
    email: 'user1@example.com',
    orders: [
      { total: 100.00 },
      { total: 200.00 },
      { total: 300.00 }
    ]
  },
  {
    name: 'User2',
    email: 'user2@example.com',
    orders: [
      { total: 400.00 },
      { total: 500.00 },
      { total: 600.00 }
    ]
  },
  {
    name: 'User3',
    email: 'user3@example.com',
    orders: [
      { total: 700.00 },
      { total: 800.00 },
      { total: 900.00 }
    ]
  },
  {
    name: 'User4',
    email: 'user4@example.com',
    orders: [
      { total: 1000.00 },
      { total: 1100.00 },
      { total: 1200.00 }
    ]
  },
  {
    name: 'User5',
    email: 'user5@example.com',
    orders: [
      { total: 1300.00 },
      { total: 1400.00 },
      { total: 1500.00 }
    ]
  },
  {
    name: 'Null User',
    email: '',
    orders: [
      { total: 1600.00 },
      { total: 1700.00 },
      { total: 1800.00 }
    ]
  }
]);