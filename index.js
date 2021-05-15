const fetch = require("node-fetch")

const url = "http://192.168.0.106:3000/object-tracker"

const getData = async url => {
  try {
    const response = await fetch(url);
    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.log(error);
  }
};

getData(url);