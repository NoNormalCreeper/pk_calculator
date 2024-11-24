def check_answer(question, user_answer) -> bool:
    try:
        question_answer = float(eval(question))
        user_answer = float(user_answer.strip())
        return abs(question_answer - user_answer) <= 0.01
    except Exception as e:
        return False

def cal_precision(correct, total):
    return round(correct / total, 2)
