from agents.feedback_agent import analyze_feedback
from agents.feature_agent import generate_features
from agents.impact_agent import estimate_impact
from agents.roadmap_agent import create_roadmap
from reports.report_generator import generate_report


def run_pipeline():

    df, complaints = analyze_feedback("data/sample_feedback.csv")

    features = generate_features(complaints)

    impact = estimate_impact(features)

    roadmap = create_roadmap(impact)

    report = generate_report(features, impact, roadmap)

    print(report)


if __name__ == "__main__":
    run_pipeline()