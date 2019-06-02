const mongoose = require('mongoose')

const authorSchema = new mongoose.Schema({
    lect_name: {type: String},
    date_time: {type: Date},
    descript: {type: String}
})

module.exports = mongoose.model('Author', authorSchema)