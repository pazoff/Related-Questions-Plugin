from cat.mad_hatter.decorators import tool, hook, plugin



@hook
def before_cat_sends_message(final_output, cat):
    global related_questions

    if related_questions != "":

     final_output["content"] = final_output["content"] + "<br><br>---<br>" + related_questions


    return final_output

@hook
def before_cat_reads_message(user_message_json: dict, cat):
    global related_questions

    def is_question(sentence):
     return sentence.endswith('?')
    
    message = user_message_json["text"]
    related_questions = ""

    if is_question(message):

     related_questions = cat.llm("write 3 related questions of the question: " + message)

    
    return user_message_json
