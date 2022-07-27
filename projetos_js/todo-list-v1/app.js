// imports
const express = require("express")
const bodyParser = require("body-parser")
const mongoose = require("mongoose")

// initializations
const app = express()

// app uses
app.set("view engine", "ejs")

app.use(bodyParser.urlencoded({ extended: true }))
app.use(express.static("public"))

// mongoose
mongoose.connect("mongodb:27017/todoListDB")
const itemsSchema = new mongoose.Schema({
	name: String,
})
const item = mongoose.model("item", itemsSchema)

const item1 = new item({
	name: "Welcome to your todolist!",
})

const item2 = new item({
	name: "Hit the + button to add an item",
})

const item3 = new item({
	name: "<--- hit this button to delete an item",
})
const defaultItems = [item1, item2, item3]

item.insertMany([item1, item2, item3], (err) => {
	if (err) {
		console.log(err)
	} else {
		console.log("success")
	}
})

// endpoint
app.get("/", function (req, res, err) {
	res.render("list", {
		listTitle: "Today",
		newListItem: items,
	})
})

// newListItem: item
app.post("/", function (req, res, err) {
	let itemBody = req.body.newItem
	if (req.body.list === "work") {
		workItem.push(itemBody)
		res.redirect("/work")
	} else {
		itemsL.push(itemBody)
		res.redirect("/")
	}
})
app.get("/work", function (req, res, err) {
	res.render("list", { newListItem: workItem, listTitle: "work" })
})

// app listen
app.listen(3000, function (req, res, err) {
	console.log("running")
})
