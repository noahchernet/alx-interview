#!/usr/bin/node
// Prints all characters of a Star Wars movie, with the episode's number passed
// as argument

const request = require('request');
const episode = process.argv[2];

request(
  'https://swapi-api.hbtn.io/api/films/' + episode,
  (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      const json = JSON.parse(body);

      listCharacters(json.characters);
    }
  }
);

const listCharacters = (characterAPIList) => {
  if (characterAPIList.length !== 0) {
    request(characterAPIList[0], (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        const json = JSON.parse(body);
        console.log(json.name);

        listCharacters(characterAPIList.slice(1));

        // return JSON.parse(body).name;
      }
    });
  }
};
