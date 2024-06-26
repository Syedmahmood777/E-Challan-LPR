const express = require("express");
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const path = require("path");
const app = express();
const cors = require("cors");
const UserModel = require("./Models/Challans");
const axios = require("axios");

app.use(express.static(path.join(__dirname, "dist")));
app.use(express.json());

dotenv.config({ path: "./config.env" });
const corsOptions = {
  origin: "http://localhost:5173",
  credentials: true, //access-control-allow-credentials:true
  optionSuccessStatus: 200,
  methods: "GET,PUT,POST,DELETE",
};
app.use(cors());
app.use(function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.setHeader(
    "Access-Control-Allow-Methods",
    "GET, POST, OPTIONS, PUT, PATCH, DELETE"
  );
  res.header(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );
  next();
});
// corsOptions
async function connect() {
  try {
    await mongoose.connect(process.env.ATLAS_URI);
    // console.log(await UserModel.find({}))
  } catch (e) {
    console.log(e);
  }
}

connect();
app.get("/getUsers", (req, res) => {
  UserModel.find()
    .then((Challans) => res.json(Challans))
    .catch((err) => res.json(err));
});

app.post("/getlpr", async (req, res) => {
  // console.log(req.body["image"]);
  try {
    const data = {
      image: req.body["image"],
    };
    const response = await axios.post(
      "https://us-central1-ec-lpr.cloudfunctions.net/predictlpr",
      data,
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    res.json(response.data);
  } catch (error) {
    console.error("Error:", error);
  }
});

app.listen(3000, () => {
  console.log("Mongo Running");
});
