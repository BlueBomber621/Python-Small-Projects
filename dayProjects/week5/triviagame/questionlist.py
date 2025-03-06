import requests
import html

def get_questions(difficulty):
    url = f"https://opentdb.com/api.php?amount=20&difficulty={difficulty}"
    response = requests.get(url)
    data = response.json()

    questions = data['results']
    for q in questions:
        q['question'] = html.unescape(q['question'])
        q['category'] = html.unescape(q['category'])
        q['incorrect_answers'] = [html.unescape(qi) for qi in q['incorrect_answers']]
        q['correct_answer'] = html.unescape(q['correct_answer'])
    return questions