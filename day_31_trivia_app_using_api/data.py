import requests


parameters = {
    'amount': 55,
    'type': 'boolean',

}
question_data = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = question_data.json()
