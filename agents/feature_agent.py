from utils.llm import ask_llm

def generate_features(complaints):

    prompt = f"""
    Users reported these issues:

    {complaints}

    Suggest product improvements and new features.
    Group similar ideas.
    """

    response = ask_llm(prompt)

    return response