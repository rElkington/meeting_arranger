const express = require('express')
const router = express.Router()
const Author = require('../models/author')

//all authors route
router.get('/', async(req, res) => {
    try{
        const authors = await Author.find({})
        res.render('authors/index', { authors: authors })
    } catch{
        res.redirect('/')
    }
    
})

//new author route
router.get('/new', (req, res) => {
    res.render('authors/new', { author: new Author()})
}) 

router.post('/', async(req, res) => {
    const author = new Author({
        lect_name: req.body.lect_name,
        date_time: req.body.date_time,
        descript: req.body.descript
    })
    try{
        const newAuthor = await author.save()
        res.redirect('authors')
    } catch{
        res.render('authors/new', {
            author: author,
        })
    }
})  

module.exports = router