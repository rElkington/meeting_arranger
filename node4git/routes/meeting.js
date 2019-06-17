const express = require('express')
const router = express.Router()
const Meeting = require('../models/meeting')
const User = require('../models/User')
const bcrypt = require('bcryptjs')
const passport = require('passport')

router.get('/', async(req, res) => {
    try{
        const meetings = await Meeting.find({})
        res.render('meetings/index', { meeting: meetings })
    } catch{
        res.redirect('/')
    }
    
})

router.get('/new', (req, res) => {
    res.render('meetings/new', { meeting: new Meeting()})
})

//Login Page
router.get('/login', (req, res) => res.render('meetings/login'))

router.post('/login', (req, res, next) => {
    passport.authenticate('local', {
      successRedirect: '/users/login',
      failureRedirect: '/meetings/new'
    })(req, res, next);
  });



router.post('/', async(req, res) => {
    const meeting = new Meeting({
        lect_name: req.body.lect_name,
        date_time: req.body.date_time,
        descript: req.body.descript
    })
    try{
        const newMeeting = await meeting.save()
        res.redirect('meetings')
    } catch{
        res.render('meetings/new', {
            meeting: meeting,
        })
    }
})  

module.exports = router