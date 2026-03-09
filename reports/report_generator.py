def generate_report(features, impact, roadmap):

    report = f"""
    PRODUCT STRATEGY REPORT
    -----------------------

    FEATURE SUGGESTIONS
    {features}

    IMPACT ANALYSIS
    {impact}

    PRODUCT ROADMAP
    {roadmap}
    """

    return report