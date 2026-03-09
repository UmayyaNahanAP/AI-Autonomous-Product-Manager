from utils.llm import ask_llm

def estimate_impact(features):

    prompt = f"""
    Evaluate the following product features.

    {features}

    For each feature give:

    - Expected user adoption
    - Business impact
    - Impact score (1-10)

    Format as list.
    """

    return ask_llm(prompt)