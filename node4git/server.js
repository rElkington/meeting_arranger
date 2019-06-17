if (process.env.NODE_ENV !== 'production'){
    require('dotenv').config()
}

const express = require('express')
const app = express()
const expressLayouts = require('express-ejs-layouts')
const bodyParser = require('body-parser')
const session = require('express-session')
const passport = require('passport');

require('./config/passport')(passport)

const indexRouter = require('./routes/index')
const meetingRouter = require('./routes/meetings')

app.use(expressLayouts)
app.set('view engine', 'ejs')
app.set('views', './views')
app.set('layout', 'layouts/layout')
app.use(express.static('public'))
app.use(bodyParser.urlencoded({ limit: '10mb', extended: false }))

const mongoose = require('mongoose')
mongoose.connect(process.env.DATABASE_URL, { useNewUrlParser: true })
const db = mongoose.connection
db.on('error', error => console.error(error))
db.once('open', error => console.log('Connected to mongoose'))

app.use(session({
    secret: 'keyboard cat',
    resave: true,
    saveUninitialized: true,
}))

app.use(passport.initialize())
app.use(passport.session())

app.use('/', indexRouter)
app.use('/meetings', meetingRouter)
app.use('/users', require('./routes/meetings'))

app.listen(process.env.PORT || 3000)