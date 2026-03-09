from utils.llm import ask_llm

def create_roadmap(impact_analysis):

    prompt = f"""
    Based on this feature impact analysis:

    {impact_analysis}

    Create a product roadmap.

    Include:

    Short Term (0-3 months)
    Mid Term (3-6 months)
    Long Term (6-12 months)

    Provide structured roadmap.
    """

    return ask_llm(prompt)