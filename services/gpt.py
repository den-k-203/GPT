import g4f
from domain.DestructObject import DestructionObject
from typing import List

def gpt_response(objects: List[DestructionObject]):
    criterion = "зброя_якою_зруйновано"
    values = "\n".join(f"{obj.__str__()}" for obj in objects)
    example = "Росія для ураження об'єктів критичної інфраструктури України використовувала Shahed. А останній раз використала ракету X-555. Висновок: противнику необхідно було саме більша кількість жертв"
    # Детальний запит з чіткими інструкціями
    prompt = (
        f"Проаналізуй наступні дані, щоб знайти екстремум за критерієм '{criterion}'.\n"
        f"Надай результат, який найкраще відповідає цьому критерію, і поясни, чому саме він є екстремумом.\n\n"
        f"Набір даних:\n{values} (Відповідь має бути українською мовою)."
        f"Приклад відповіді: {example}"
    )

    # Виклик API для отримання відповіді
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4o,
        messages=[{"role": "user", "content": prompt}]
    )

    if response == "Generated by BLACKBOX.AI, try unlimited chat https://www.blackbox.ai":
        return gpt_response(objects)
    elif 'error' in response:
        return  gpt_response(objects)
    elif 'BLACKBOX.AI' in response:
        return gpt_response(objects)
    return response

