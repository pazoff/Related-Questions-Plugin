from cat.mad_hatter.decorators import tool, hook, plugin

# Global variable to store related questions
global related_questions

# Hook that is executed before Cat sends a message
@hook
def before_cat_sends_message(final_output, cat):
    # Access the global variable
    global related_questions

    # Check if there are related questions
    if related_questions != "":
        # Add a separator and display related questions in the final output
        final_output["content"] = final_output["content"] + "<br><br>---<br>" + related_questions

    # Return the modified final output
    return final_output

# Hook that is executed before Cat reads a message
@hook
def before_cat_reads_message(user_message_json: dict, cat):
    # Access the global variable
    global related_questions

    # Function to check if a sentence is a question
    def is_question(sentence):
        return sentence.endswith('?')

    # Extract the text message from the user's message JSON
    message = user_message_json["text"]

    # Initialize an empty string to store related questions
    related_questions = ""

    # Check if the user's message is a question
    if is_question(message):
        # Use Cat's llm method to generate related questions with links
        related_questions = cat.llm("write several related questions of the question: " + message +
                                    " Return every question with a link <a href and parameter for https://www.phind.com/search?q=question. The link should open in a new window")

    # Return the original user's message JSON
    return user_message_json
