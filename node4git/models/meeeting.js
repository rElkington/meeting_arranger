const mongoose = require('mongoose')

const meetingSchema = new mongoose.Schema({
    lect_name: {type: String},
    date_time: {type: Date},
    descript: {type: String}
})

module.exports = mongoose.model('Author', meetingSchema)