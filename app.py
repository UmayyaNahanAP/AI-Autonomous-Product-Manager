import streamlit as st
from agents.feedback_agent import analyze_feedback
from agents.feature_agent import generate_features
from agents.impact_agent import estimate_impact
from agents.roadmap_agent import create_roadmap

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.title("AI Autonomous Product Manager")

uploaded_file = st.file_uploader("Upload User Feedback CSV")

if uploaded_file:

    with open("temp.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())

    df, complaints = analyze_feedback("temp.csv")

    st.subheader("Feedback Analysis")
    st.write(df)

    if st.button("Generate Product Strategy"):

        features = generate_features(complaints)
        impact = estimate_impact(features)
        roadmap = create_roadmap(impact)

        st.subheader("Feature Suggestions")
        st.write(features)

        st.subheader("Impact Analysis")
        st.write(impact)

        st.subheader("Product Roadmap")
        st.write(roadmap)

        # ---------- CREATE PDF ----------
        pdf_file = "product_strategy_report.pdf"

        styles = getSampleStyleSheet()
        elements = []

        elements.append(Paragraph("AI Autonomous Product Manager Report", styles['Title']))
        elements.append(Spacer(1,20))

        elements.append(Paragraph("Feature Suggestions", styles['Heading2']))
        elements.append(Paragraph(features.replace("\n","<br/>"), styles['BodyText']))
        elements.append(Spacer(1,20))

        elements.append(Paragraph("Impact Analysis", styles['Heading2']))
        elements.append(Paragraph(impact.replace("\n","<br/>"), styles['BodyText']))
        elements.append(Spacer(1,20))

        elements.append(Paragraph("Product Roadmap", styles['Heading2']))
        elements.append(Paragraph(roadmap.replace("\n","<br/>"), styles['BodyText']))

        doc = SimpleDocTemplate(pdf_file)
        doc.build(elements)

        # ---------- DOWNLOAD BUTTON ----------
        with open(pdf_file, "rb") as f:
            st.download_button(
                label="Download Product Strategy Report (PDF)",
                data=f,
                file_name="product_strategy_report.pdf",
                mime="application/pdf"
            )

# import streamlit as st
# from agents.feedback_agent import analyze_feedback
# from agents.feature_agent import generate_features
# from agents.impact_agent import estimate_impact
# from agents.roadmap_agent import create_roadmap

# st.title("AI Autonomous Product Manager")

# uploaded_file = st.file_uploader("Upload User Feedback CSV")

# if uploaded_file:

#     with open("temp.csv","wb") as f:
#         f.write(uploaded_file.getbuffer())

#     df, complaints = analyze_feedback("temp.csv")

#     st.subheader("Feedback Analysis")
#     st.write(df)

#     if st.button("Generate Product Strategy"):

#         features = generate_features(complaints)
#         impact = estimate_impact(features)
#         roadmap = create_roadmap(impact)

#         st.subheader("Feature Suggestions")
#         st.write(features)

#         st.subheader("Impact Analysis")
#         st.write(impact)

#         st.subheader("Product Roadmap")
#         st.write(roadmap)