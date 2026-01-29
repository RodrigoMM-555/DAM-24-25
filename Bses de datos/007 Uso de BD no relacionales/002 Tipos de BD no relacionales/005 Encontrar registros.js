// Dame todos
db.facturas.find()

// Dame la primera
db.facturas.findOne()

// Select con where -> Vete a facturas y encuentrame algo con una condicion
db.facturas.findOne({nombre:'Jose Vicente'})