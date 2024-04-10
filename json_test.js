let test_json = require('./test.json')

console.log(test_json)

const new_json_str = '{ "Name": "Marine", "Armor": 1, "Armor_Type": "Light", "Damage": 5, "isDead": false }'

const new_json_obj = JSON.parse(new_json_str)

console.log(new_json_obj)